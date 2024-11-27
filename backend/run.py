# backend/run.py

from app import app

# Import your routes and blueprints
from routes.send_reminders import send_reminders_bp
from routes.auth import auth
from routes.foodAdd import food_bp
from routes.householdRoutes import household_bp
# Import other blueprints as needed
# from routes.other_routes import other_bp

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(send_reminders_bp)
app.register_blueprint(household_bp)
app.register_blueprint(food_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
