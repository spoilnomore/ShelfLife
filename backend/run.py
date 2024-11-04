from flask import Flask
from flask_cors import CORS
from models import db
from routes.auth import auth
from routes.foodAdd import food_bp
from flask import send_from_directory

app = Flask(__name__)

# Enable CORS with more explicit configuration
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pantryowner:spoilnomore@shelfdb:5432/shelflife'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db.init_app(app)

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(food_bp)



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
