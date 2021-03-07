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
        contact = ContactModel.find_by_email(email)
        if contact:
            return {"message": f"ERROR: Contact already exists <email={email}>"}

        contact_json = request.get_json()
        contact_json["email"] = email
        contact_json["phone"] = "+52" + contact_json["phone"]

        try:
            contact = contact_schema.load(contact_json)
        except ValidationError as err:
            return err.message

        try:
            contact.save_to_db()
        except:
            return {"message": f"ERROR: Couldn't save to database <email={email}>"}

        return contact_schema.dump(contact)

    def put(self, email: str):
        contact_json = request.get_json()
        contact = ContactModel.find_by_email(email)
        if contact:
            contact.first_name = contact_json["first_name"]
            contact.last_name = contact_json["last_name"]
            contact.phone = "+52" + contact_json["phone"]
        else:
            contact_json["email"] = email
            contact = contact_schema.load(contact_json)
        contact.save_to_db()
        return contact_schema.dump(contact)

    def delete(self, email: str):
        contact = ContactModel.find_by_email(email)
        if contact:
            contact.delete_from_db()
            return {"message": f"deleted contact <email={email}>"}
        return {"message": f"ERROR: Couldn't delete from database <email={email}>"}

class ContactList(Resource):
    def get(self):
        return {"content": contact_list_schema.dump(ContactModel.find_all())}
