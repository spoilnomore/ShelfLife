from flask import Blueprint, request, jsonify
from models import db
from models.household import Household
from models.user import User




household_bp = Blueprint('household', __name__)

@household_bp.route('/households', methods=['GET'])
def get_all_households():
    households = Household.query.all()
    household_data = [{"id": household.id, "name": household.household_name} for household in households]
    print('Household data:', household_data)
    return jsonify(household_data)



@household_bp.route('/households/<int:household_id>/members', methods=['GET'])
def get_household_members(household_id):
    # Check if the household exists
    household = Household.query.get(household_id)
    if not household:
        return jsonify({"error": "Household not found"}), 404

    # Get members of the household
    members = User.query.filter_by(household_id=household_id).all()
    if not members:
        return jsonify({"error": "No members found in this household"}), 404

    member_data = [{"id": member.id, "username": member.username} for member in members]
    print(f"Household members: {member_data}")
    return jsonify({"members": member_data}), 200

