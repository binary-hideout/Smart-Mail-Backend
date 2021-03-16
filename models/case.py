from typing import List
from db import db

class CaseModel(db.Model):
    __tablename__ = "cases"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False) 

    def __repr__(self):
        return f"<Case={self.title}>"

    @classmethod
    def find_by_title(cls, title: str) -> "CaseModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_all(cls) -> List["CaseModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
