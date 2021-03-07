from flask import request
from flask_restful import Resource
from schemas.contact import ContactSchema
from models.contact import ContactModel
from marshmallow import ValidationError

contact_schema = ContactSchema()
contact_list_schema = ContactSchema(many=True)

class Contact(Resource):
    def get(self, email: str):
        contact = ContactModel.find_by_email(email)
        if contact:
            return contact_schema.dump(contact)
        return {"message": f"ERROR: Couldn't find requested contact <email={email}>"}

    def post(self, email: str):
        pass

    def put(self, email: str):
        return {"content": f"PUT: contact <email={email}>"}

    def delete(self, email: str):
        return {"content": f"DELETE: contact <email={email}>"}


class ContactList(Resource):
    def get(self):
        return {"content": contact_list_schema.dump(ContactModel.find_all())}
