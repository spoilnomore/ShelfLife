from flask import Flask, send_from_directory
from flask_cors import CORS
from models import db
from routes.auth import auth
from routes.foodAdd import food_bp
from routes.householdRoutes import household_bp
import logging
import os

# Ensure the logs directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, "app.log")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Adjust to INFO, WARNING, etc., as needed
    format='%(asctime)s - %(levelname)s - %(message)s',  # Include timestamps
    handlers=[
        logging.StreamHandler(),  # Write to console (stdout)
        logging.FileHandler(log_file_path)  # Write to app.log
    ]
)

app = Flask(__name__)

# Enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pantryowner:spoilnomore@shelfdb:5432/shelflife'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db.init_app(app)

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(food_bp)
app.register_blueprint(household_bp)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == "__main__":
    app.run()
