from flask import Blueprint, request, jsonify
from models import db
from models.user import User
from models.household import Household

auth = Blueprint('auth', __name__)

@auth.route('/check-user', methods=['POST', 'OPTIONS'])
def check_user():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    google_id = data.get('google_id')
    email = data.get('email')

    # Check if the user exists
    user = User.query.filter_by(google_id=google_id).first()
    if not user:
        return jsonify({'isNewUser': True})
    
    # If user exists, join with the household table to get household name
    household_name = None
    if user.household_id:
        household = Household.query.filter_by(id=user.household_id).first()
        if household:
            household_name = household.household_name

    # Return existing user data, including the household name if it exists
    return jsonify({'user': {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'google_id': user.google_id,
        'household_name': household_name
    }, 'isNewUser': False})



@auth.route('/create-user', methods=['POST'])
def create_user():
    data = request.json
    google_id = data.get('google_id')
    email = data.get('email')
    username = data.get('username')
    household_id = data.get('household_id')
    household_name = data.get('household_name')
    create_new_household = data.get('create_new_household')  # Boolean value

    if not username or (create_new_household and not household_name):
        return jsonify({'error': 'Username and household name are required'}), 400

    # Handle creating or joining a household
    household = None
    if create_new_household:
        # Create a new household
        household = Household.query.filter_by(household_name=household_name).first()
        if household:
            return jsonify({'error': 'Household name already exists'}), 400
        household = Household(household_name=household_name)
        db.session.add(household)
        db.session.commit()
    else:
        # Join an existing household
        if not household_id:
            return jsonify({'error': 'Household ID is required'}), 400
        household = Household.query.get(household_id)
        if not household:
            return jsonify({'error': 'Household not found'}), 404

    # Create new user in the database with the household_id
    try:
        new_user = User(
            username=username,
            email=email,
            google_id=google_id,
            household_id=household.id
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'user': {
            'id': new_user.id,
            'username': new_user.username,
            'email': new_user.email,
            'google_id': new_user.google_id,
            'household_name': household.household_name,
            'household_id': household.id
        }, 'isNewUser': False})

    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({'error': 'Failed to create user'}), 500
