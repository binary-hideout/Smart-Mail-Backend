from flask import Flask
from flask_restful import Api
from resources.contact import Contact, ContactList

app = Flask(__name__)
api = Api(app)

api.add_resource(Contact, "/contact/<string:email>")
api.add_resource(ContactList, "/contacts")

if __name__ == "__main__":
    app.run(debug=True)
