from flask import request, make_response, render_template, redirect, url_for
from flask_restful import Resource
from smartmail.schemas.schemas import CaseSchema
from smartmail.models.case import CaseModel
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

case_schema = CaseSchema()
case_list_schema = CaseSchema(many=True)


class Case(Resource):
    @jwt_required()
    def get(self, title: str):
        case = CaseModel.find_by_title(title)
        if case:
            # return case_schema.dump(case), 200
            headers = {"Content-Type": "text-html"}
            return make_response(
                render_template("case.html", result=case_schema.dump(case)),
                200,
                headers,
            )
        return {"message": f"ERROR: Couldn't find requested case <title={title}>"}, 400
        # headers = {"Content-Type": "text-html"}
        # return make_response(
        #     render_template("400.html"),
        #     400,
        #     headers,
        # )

    @jwt_required()
    def post(self, title: str):
        case_data = request.form.copy()
        case = CaseModel.find_by_title(title)
        if case:
            case.title = title
            case.description = case_data["description"]
            case.tag_id = case_data["tag_id"]
            case.contact_id = case_data["contact_id"]
        else:
            case_data["title"] = title
            case = case_schema.load(case_data)
        case.save_to_db()
        # return case_schema.dump(case), 200
        # headers = {"Content-Type": "text-html"}
        # return make_response(
        #     render_template("case.html", result=case_schema.dump(case)),
        #     200,
        #     headers,
        # )
        return redirect(url_for('case', title=title))


class CaseDelete(Resource):
    @jwt_required()
    def get(self, title: str):
        case = CaseModel.find_by_title(title)
        if case:
            case.delete_from_db()
            # return {"message": f"deleted tag <title={title}>"}, 200
            headers = {"Content-Type": "text-html"}
            return redirect(url_for("caselist"))
        # return {"message": "ERROR: Couldn't delete from database"}, 404
        # headers = {"Content-Type": "text-html"}
        # return make_response(
        #     render_template("404.html"),
        #     404,
        #     headers,
        # )
        return redirect(url_for('caselist'))

class CaseList(Resource):
    @jwt_required()
    def get(self):
        # return {"content": case_list_schema.dump(CaseModel.find_all())}, 200
        headers = {"Content-Type": "text-html"}
        return make_response(
            render_template(
                "cases.html", results=case_list_schema.dump(CaseModel.find_all())
            ),
            200,
            headers,
        )

    @jwt_required()
    def post(self):
        case_data = request.form.copy()
        title = case_data["title"]
        case = CaseModel.find_by_title(title)
        if case:
            return {"message": f"ERROR: Case already exists <title={title}>"}
        try:
            case = case_schema.load(case_data)
        except ValidationError as err:
            return err.messages

        try:
            case.save_to_db()
        except:
            return {"message": f"ERROR: Couldn't save to database"}, 500
            # headers = {"Content-Type": "text-html"}
            # return make_response(
            #     render_template("500.html"),
            #     500,
            #     headers,
            # )
        # return case_schema.dump(case), 201
        return redirect(url_for("caselist"))
