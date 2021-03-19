from flask import request
from flask_restful import Resource
from schemas.schemas import CaseSchema
from models.case import CaseModel
from marshmallow import ValidationError

case_schema = CaseSchema()
case_list_schema = CaseSchema(many=True)


class Case(Resource):
    def get(self, title: str):
        case = CaseModel.find_by_title(title)
        if case:
            return case_schema.dump(case), 200
        return {"message": f"ERROR: Couldn't find requested case <title={title}>"}, 400

    def post(self, title: str):
        case = CaseModel.find_by_title(title)
        if case:
            return {"message": f"ERROR: Case already exists <title={title}>"}
        case_json = request.get_json()
        case_json["title"] = title
        try:
            case = case_schema.load(case_json)
        except ValidationError as err:
            return err.messages

        try:
            case.save_to_db()
        except:
            return {"message": f"ERROR: Couldn't save to database"}, 500
        return case_schema.dump(case), 201

    def put(self, title: str):
        case_json = request.get_json()
        case = CaseModel.find_by_title(title)
        if case:
            case.title = case_json["title"]
            case.description = case_json["description"]
            case.tag_id = case_json["tag_id"]
            case.contact_id = case_json["contact_id"]
        else:
            case_json["title"] = title
            case = case_schema.load(case_json)
        case.save_to_db()
        return case_schema.dump(case), 200

    def delete(self, title: str):
        case = CaseModel.find_by_name(title)
        if case:
            case.delete_from_db()
            return {"message": f"deleted tag <title={title}>"}, 200
        return {"message": "ERROR: Couldn't delete from database"}, 404


class CaseList(Resource):
    def get(self):
        return {"content": case_list_schema.dump(CaseModel.find_all())}, 200
