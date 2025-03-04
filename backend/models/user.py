from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    google_id = db.Column(db.String(4000), unique=True, nullable=False)
    household_id = db.Column(db.Integer, db.ForeignKey('households.id'), nullable=True)

    # Define relationship to access household details if needed
    household = db.relationship('Household', backref='members', lazy=True)
