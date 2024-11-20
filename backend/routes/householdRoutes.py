from flask import Blueprint, request, jsonify
from models import db
from models.household import Household
from models.user import User




household_bp = Blueprint('household', __name__)


@household_bp.route('/householdMembers', methods=['GET'])
def get_household_members():
    household_id = request.args.get('household_id', type=int)
    if not household_id:
        return jsonify({"error": "household_id is required"}), 400

    members = User.query.filter_by(household_id=household_id).all()
    if not members:
        return jsonify({"error": "members is required"}), 400

    member_data = [{"id": member.id, "username": member.username} for member in members]
    logging.debug(f"Household members: {member_data}")
    return jsonify(member_data)



