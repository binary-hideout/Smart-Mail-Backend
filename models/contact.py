from typing import List
from apps.db import db
from datetime import datetime


class ContactModel(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    created = db.Column(db.DateTime, default=datetime.today())
    cases = db.relationship("CaseModel", backref="contact", lazy=True)

    def __repr__(self):
        return f"<Contact={self.email}>"

    @classmethod
    def find_by_email(cls, email: str) -> "ContactModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_all(cls) -> List["ContactModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
