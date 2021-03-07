from db import db
import datetime

class ContactModel(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(25), default="To be resolved")