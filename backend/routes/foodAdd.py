from flask import Blueprint, request, jsonify
from models import db
from models.food import Food  
import os

food_bp = Blueprint('food', __name__)

@food_bp.route('/foodAdd', methods=['POST'])
def food_add():
    try:
        title = request.form.get('title')
        location = request.form.get('location')
        owner = request.form.get('owner')
        expiration_date = request.form.get('expiration_date')
        sharing = request.form.get('sharing')
        image = request.files.get('image')  # Retrieve the file

        if not title or not location or not owner or not expiration_date or not sharing:
            return jsonify({"error": "Missing required fields"}), 400

        # Save image to file system if provided
        image_path = None
        if image:
            image_folder = 'uploads'
            os.makedirs(image_folder, exist_ok=True)
            image_path = os.path.join(image_folder, image.filename)
            image.save(image_path)

        # Create and save new food item
        new_food = Food(
            title=title,
            location=location,
            owner=owner,
            expiration_date=expiration_date,
            sharing=sharing,
            image_path=image_path
        )
        db.session.add(new_food)
        db.session.commit()

        return jsonify({"message": "Food item added successfully"}), 201
    except Exception as e:
        print(f"Error adding food: {e}")
        return jsonify({"error": f"Failed to food item {e}"}), 500


@food_bp.route('/foods', methods=['GET'])
def get_foods():
    foods = Food.query.all()
    food_data = [{
        "id": food.id,
        "title": food.title,
        "location": food.location,
        "owner": food.owner,
        "expiration_date": food.expiration_date.isoformat(),
        "sharing": food.sharing,
        "image_location": food.image_path.split('/')[-1] if food.image_path else None  # Send just the image filename
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