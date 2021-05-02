from flask import request, make_response, render_template, redirect, url_for
from flask_restful import Resource

class Home(Resource):
    def get(self):
        headers = {"Content-Type": "text-html"}
        return make_response(
            render_template("home.html"),
            200,
            headers,
        )