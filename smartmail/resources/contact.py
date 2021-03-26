from flask import request
from flask_restful import Resource
from smartmail.schemas.schemas import ContactSchema
from smartmail.models.contact import ContactModel
from marshmallow import ValidationError

contact_schema = ContactSchema()
contact_list_schema = ContactSchema(many=True)


class Contact(Resource):
    def get(self, email: str):
        contact = ContactModel.find_by_email(email)
        if contact:
            return contact_schema.dump(contact), 200
        return {"message": f"ERROR: Couldn't find requested contact <email={email}>"}, 404

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
            return {"message": f"ERROR: Couldn't save to database <email={email}>"}, 500

        return contact_schema.dump(contact), 201

    def put(self, email: str):
        contact_json = request.get_json()
        contact = ContactModel.find_by_email(email)
        if contact:
            contact.first_name = contact_json["first_name"]
            contact.last_name = contact_json["last_name"]
            if contact_json["phone"][:3] == "+52":
                contact.phone = contact_json["phone"]
            else:
                contact.phone = "+52" + contact_json["phone"]
        else:
            contact_json["email"] = email
            contact_json["phone"] = "+52" + contact_json["phone"]
            contact = contact_schema.load(contact_json)
        contact.save_to_db()
        return contact_schema.dump(contact), 200

    def delete(self, email: str):
        contact = ContactModel.find_by_email(email)
        if contact:
            contact.delete_from_db()
            return {"message": f"deleted contact <email={email}>"}, 200
        return {"message": f"ERROR: Couldn't delete from database <email={email}>"}, 404


class ContactList(Resource):
    def get(self):
        return {"content": contact_list_schema.dump(ContactModel.find_all())}, 200
