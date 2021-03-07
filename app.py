from flask import Flask
from flask_restful import Api

from resources.contact import Contact, ContactList

from db import db

app = Flask(__name__)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Contact, "/contact/<string:email>")
api.add_resource(ContactList, "/contacts")

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
