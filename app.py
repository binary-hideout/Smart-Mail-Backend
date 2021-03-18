from flask import Flask
from flask_restful import Api

from resources.contact import Contact, ContactList
from resources.case import Case, CaseList
from resources.tag import Tag, TagList

from db import db
from ma import ma

from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv(".env", verbose=True)
app.config.from_object("default_settings")
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)
db.init_app(app)
ma.init_app(app)

# For production
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Contact, "/contact/<string:email>")
api.add_resource(ContactList, "/contacts")
api.add_resource(Case, "/case/<string:title>")
api.add_resource(CaseList, "/cases")
api.add_resource(Tag, "/tag/<string:title>")
api.add_resource(TagList, "/tags")

# For local development
if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True)
