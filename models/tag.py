from db import db

class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    cases = db.relationship('Case', backref="tag", lazy=True)

    def __repr__(self):
        return f"<Tag={self.title}>"