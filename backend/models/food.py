from datetime import datetime
from models import db
from sqlalchemy.orm import relationship

class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    owner = db.Column(db.String(255), nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    sharing = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key to Households table
    household_id = db.Column(db.Integer, db.ForeignKey('households.id'), nullable=True)
    household = relationship('Household', back_populates='food_items')

    def __repr__(self):
        return f"<Food {self.title} owned by {self.owner}>"
