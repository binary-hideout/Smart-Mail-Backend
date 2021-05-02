from flask import request, make_response, render_template, redirect, url_for
from flask_restful import Resource
from smartmail.schemas.schemas import ContactSchema
from smartmail.models.contact import ContactModel
from smartmail.forms.contact import ContactCreateForm, ContactUpdateForm
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

contact_schema = ContactSchema()
contact_list_schema = ContactSchema(many=True)


class Contact(Resource):
    # @jwt_required()
    def get(self, email: str):
        contact_form = ContactUpdateForm()
        contact = ContactModel.find_by_email(email)
        if contact:
            # return contact_schema.dump(contact), 200
            headers = {"Content-Type": "text-html"}
            return make_response(
                render_template("contact.html", result=contact_schema.dump(contact), form=contact_form),
                200,
                headers,
            )
        return {
            "message": f"ERROR: Couldn't find requested contact <email={email}>"
        }, 404

    # @jwt_required()
    def post(self, email: str):
        contact_form = ContactUpdateForm()
        if contact_form.validate_on_submit():
            contact_data = request.form.copy()
            contact = ContactModel.find_by_email(email)
            if contact:
                contact.first_name = contact_data["first_name"]
                contact.last_name = contact_data["last_name"]
                if contact_data["phone"][:3] == "+52":
                    contact.phone = contact_data["phone"]
                else:
                    contact.phone = "+52" + contact_data["phone"]
            else:
                contact_data["email"] = email
                contact_data["phone"] = "+52" + contact_data["phone"]
                contact = contact_schema.load(contact_data)
            contact.save_to_db()
            return redirect(url_for("contactlist"))


class ContactDelete(Resource):
    # @jwt_required()
    def get(self, email: str):
        contact = ContactModel.find_by_email(email)
        if contact:
            contact.delete_from_db()
            # return {"message": f"deleted contact <email={email}>"}, 200
            return redirect(url_for("contactlist"))
        return {"message": f"ERROR: Couldn't delete from database <email={email}>"}, 404


class ContactList(Resource):
    # @jwt_required()
    def get(self):
        contact_form = ContactCreateForm()
        headers = {"Content-Type": "text-html"}
        return make_response(
            render_template(
                "contacts.html",
                results=contact_list_schema.dump(ContactModel.find_all()),
                form=contact_form,
            ),
            200,
            headers,
        )

    # @jwt_required()
    def post(self):
        contact_form = ContactCreateForm()
        if contact_form.validate_on_submit():
            contact_data = request.form.copy()
            contact_data["phone"] = "+52" + contact_data["phone"]
            email = contact_data["email"]
            contact = ContactModel.find_by_email(email)
            if contact:
                return {"message": f"ERROR: Contact already exists <email={email}>"}

            # try:
            contact = contact_schema.load(contact_data)
            # except ValidationError as err:
            #     return err

            try:
                contact.save_to_db()
            except:
                return {"message": f"ERROR: Couldn't save to database <email={email}>"}, 500

            # return contact_schema.dump(contact), 201
            # headers = {"Content-Type": "text-html"}
            # return make_response(
            #     render_template("contact.html", result=contact_schema.dump(contact)),
            #     201,
            #     headers,
            # )
            return redirect(url_for("contactlist"))