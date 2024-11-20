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
            household_id = household.id

    # Return existing user data, including the household name if it exists
    return jsonify({'user': {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'google_id': user.google_id,
        'household_name': household_name,
        'household_id': household_id
    }, 'isNewUser': False})



@auth.route('/create-user', methods=['POST'])
def create_user():
    data = request.json
    google_id = data.get('google_id')
    email = data.get('email')
    username = data.get('username')
    household_name = data.get('household_name')
    create_new_household = data.get('create_new_household')  # boolean value

    if not username or not household_name:
        return jsonify({'error': 'Username and household name are required'}), 400

    # Handle creating or joining a household
    household = Household.query.filter_by(household_name=household_name).first()
    
    if create_new_household:
        if household:
            return jsonify({'error': 'Household name already exists. Please choose another name or join this household.'}), 400
        # Create a new household
        household = Household(household_name=household_name)
        db.session.add(household)
        db.session.commit()
    
    if not household:
        return jsonify({'error': 'Household not found. Please check the name or create a new household.'}), 404

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
            'household_name': household.household_name
        }, 'isNewUser': False})
    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({'error': 'Failed to create user'}), 500

