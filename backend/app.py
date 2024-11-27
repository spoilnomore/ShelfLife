import os
from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from models import db
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Adjust to INFO, WARNING, etc., as needed
    format='%(asctime)s - %(levelname)s - %(message)s',  # Include timestamps
    handlers=[
        logging.StreamHandler(),  # Write to console (stdout)
    ]
)

# Load environment variables from .env for Flask
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Initialize extensions
mail = Mail()
cors = CORS()
db.init_app

logging.info('hi')

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'postgresql://pantryowner:spoilnomore@shelfdb:5432/shelflife'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Email configuration
    app.config.update(
        MAIL_SERVER=os.getenv('MAIL_SERVER'),
        MAIL_PORT=int(os.getenv('MAIL_PORT', 587)),
        MAIL_USE_TLS=os.getenv('MAIL_USE_TLS') == 'True',
        MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
        MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
        MAIL_DEFAULT_SENDER=os.getenv('MAIL_DEFAULT_SENDER', 'noreply@shelflife.com')
    )

    # Celery configuration
    app.config.update(
        CELERY_BROKER_URL=os.getenv('CELERY_BROKER_URL', 'redis://redisserver:6379/0'),
        CELERY_RESULT_BACKEND=os.getenv('CELERY_RESULT_BACKEND', 'redis://redisserver:6379/0'),
    )

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    cors.init_app(app)

    return app


def make_celery(app):
    # Reload environment variables for Celery workers
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    celery = Celery(
        app.import_name,
        backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://redisserver:6379/0'),
        broker=os.getenv('CELERY_BROKER_URL', 'redis://redisserver:6379/0'),
    )

    # Ensure tasks run within Flask app context
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = create_app()
celery = make_celery(app)

# Import tasks explicitly to register them
with app.app_context():
    import tasks
