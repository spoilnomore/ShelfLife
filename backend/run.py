from flask import Flask
from flask_cors import CORS
from models import db
from routes.auth import auth

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
