from flask import Blueprint, request, jsonify
from models import db
from models.food import Food  
import os
from flask import send_from_directory


food_bp = Blueprint('food', __name__)

@food_bp.route('/foodAdd', methods=['POST'])
def food_add():
    try:
        title = request.form.get('title')
        location = request.form.get('location')
        owner = request.form.get('owner')
        expiration_date = request.form.get('expiration_date')
        sharing = request.form.get('sharing')
        household_id = request.form.get('household_id')

        # Get the file
        image = request.files.get('image')

        if not household_id:
            return jsonify({"error": "household_id is required"}), 400

        if not title or not location or not owner or not expiration_date or not sharing:
            return jsonify({"error": "Missing required fields"}), 400

        # Save image to file system if provided
        image_path = None
        if image:
            image_folder = os.path.join(os.getcwd(), 'uploads')  # Absolute path to 'uploads'
            os.makedirs(image_folder, exist_ok=True)  # Ensure folder exists
            image_path = os.path.join(image_folder, image.filename)
            image.save(image_path)

        # Create and save new food item
        new_food = Food(
            title=title,
            location=location,
            owner=owner,
            expiration_date=expiration_date,
            sharing=sharing,
            image_path=image_path,
            household_id=household_id
        )
        db.session.add(new_food)
        db.session.commit()

        return jsonify({"message": "Food item added successfully"}), 201
    except Exception as e:
        print(f"Error adding food: {e}")
        return jsonify({"error": f"Failed to add food item: {e}"}), 500


@food_bp.route('/foods', methods=['GET'])
def get_foods():
    household_id = request.args.get('household_id', type=int)
    if not household_id:
        return jsonify({"error": "household_id is required"}), 400

    foods = Food.query.filter_by(household_id=household_id).all()
    food_data = [{
        "id": food.id,
        "title": food.title,
        "location": food.location,
        "owner": food.owner,
        "expiration_date": food.expiration_date.isoformat(),
        "sharing": food.sharing,
        "image_location": f"http://localhost:8081/uploads/{food.image_path.split('/')[-1]}" if food.image_path else None

    } for food in foods]
    return jsonify(food_data)




@food_bp.route('/foods/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    food = Food.query.get(food_id)
    if food is None:
        return jsonify({"error": "Food item not found"}), 404
    
    # Delete the image file if it exists
    if food.image_path and os.path.exists(food.image_path):
        os.remove(food.image_path)
    
    db.session.delete(food)
    db.session.commit()
    return jsonify({"message": "Food item deleted successfully"}), 200


@food_bp.route('/uploads/<path:filename>', methods=['GET'])
def serve_upload(filename):
    uploads_dir = os.path.join(os.getcwd(), 'uploads')  # Absolute path to 'uploads'
    return send_from_directory(uploads_dir, filename)