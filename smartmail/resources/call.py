from os import system
from os.path import abspath, join, dirname
from time import sleep
from gtts import gTTS
import sys

from flask import request, make_response, render_template, redirect, url_for
from flask_restful import Resource
from smartmail.schemas.schemas import ContactSchema
from smartmail.models.contact import ContactModel
from smartmail.apps.android_manager import phone_call, save_text, play_sound, adb_exec_path, mpg123_exec_path, sounds_dir_path
from smartmail.forms.call import CallForm

contact_schema = ContactSchema()

class Call(Resource):
    def get(self, email: str):
        call_form  = CallForm()
        contact = ContactModel.find_by_email(email)
        if contact:
            # return contact_schema.dump(contact), 200
            headers = {"Content-Type": "text-html"}
            return make_response(
                render_template("call.html", result=contact_schema.dump(contact), form=call_form),
                200,
                headers,
            )
        return {
            "message": f"ERROR: Couldn't find requested contact <email={email}>"
        }, 404

    def post(self, email: str):
        call_form = CallForm()
        if call_form.validate_on_submit():
            call_data = request.form.copy()
            contact = ContactModel.find_by_email(email)
            if contact:
                file_path = save_text(call_data['message'], call_data['language'], 'message.mp3')
                phone_call(adb_exec_path, "7120018020022742", contact.phone)
                sleep(45)
                play_sound(mpg123_exec_path, file_path)
            return redirect(url_for('caselist'))