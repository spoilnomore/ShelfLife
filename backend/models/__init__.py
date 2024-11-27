from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .household import Household
from .food import Food
