from typing import List
from db import db

class TagModel(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    cases = db.relationship('Case', backref="tag", lazy=True)

    def __repr__(self):
        return f"<Tag={self.title}>"

    @classmethod
    def find_by_title(cls, title: str) -> "TagModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_all(cls) -> List["TagModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()