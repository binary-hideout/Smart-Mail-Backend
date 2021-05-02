from flask import request, make_response, render_template, redirect, url_for
from flask_restful import Resource
from smartmail.forms.myform import MyForm

class Test(Resource):
    def get(self):
        form = MyForm()
        headers = {"Content-Type": "text-html"}
        return make_response(
            render_template("submit.html", form=form),
            200,
            headers,
        )

    def post(self):
        form = MyForm()
        if form.validate_on_submit():
            return redirect(url_for('caselist'))