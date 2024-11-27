from . import db
from sqlalchemy.orm import relationship

class Household(db.Model):
    __tablename__ = 'households'
    id = db.Column(db.Integer, primary_key=True)
    household_name = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationship to Food
    food_items = relationship('Food', back_populates='household')
