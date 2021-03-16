from flask import request
from flask_restful import Resource
from schemas.case import CaseSchema
from models.case import CaseModel
from marshmallow import ValidationError

case_schema = CaseSchema()
case_list_schema = CaseSchema(many=True)

class Case(Resource):
    def get(self, title: str):
        case = CaseModel.find_by_title(title)
        if case:
            return case_schema.dump(case)
        return {"message": f"ERROR: Couldn't find requested case <title={title}>"}

    def post(self, title: str):
        case = CaseModel.find_by_title(title)
        if case:
            return {"message": f"ERROR: Case already exists <title={title}>"}
        case_json = request.get_json()
        case_json["title"] = title
        try:
            case = case_schema.load(case_json)
        except ValidationError as err:
            return err.message

        try:
            case.save_to_db()
        except:
            return {"message": f"ERROR: Couldn't save to database"}
        return case_schema.dump(case)

    def put(self, title: str):
        case_json = request.get_json()
        case = CaseModel.find_by_title(title)
        if case:
            case.title = case_json["title"]
            case.description = case_json["description"]
            case.tag_id = case_json["tag"].id
            case.contact_id = case_json["contact"].id
        else:
            case_json["title"] = title
            case = case_schema.load(case_json)
        case.save_to_db()
        return case_schema.dump(case)

    def delete(self, title: str):
        case = CaseModel.find_by_name(title)
        if case:
            case.delete_from_db()
            return {"message": f"deleted tag <title={title}>"}
        return {"message": "ERROR: Couldn't delete from database"}

class CaseList(Resource):
    def get(self):
        return {"content": case_list_schema.dump(CaseModel.find_all())}