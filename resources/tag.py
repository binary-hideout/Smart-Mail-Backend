from flask import request
from flask_restful import Resource
from schemas.tag import TagSchema
from models.tag import TagModel
from marshmallow import ValidationError

tag_schema = TagSchema()
tag_list_schema = TagSchema(many=True)

class Tag(Resource):
    def get(self, name: str):
        tag = TagModel.find_by_name(name)
        if tag:
            return tag_schema.dump(tag)
        return {"message": f"ERROR: Couldn't find requested tag <tag={tag}>"}

    def post(self, name: str):
        tag = TagModel.find_by_name(name)
        if tag:
            return {"message": f"ERROR: Tag already exists <tag={tag}>"}
        tag_json = request.get_json()
        tag_json["name"] = name
        try:
            tag = tag_schema.load(tag_json)
        except ValidationError as err:
            return err.message

        try:
            tag.save_to_db()
        except:
            return {"message": f"ERROR: Couldn't save to database"}
        return tag_schema.dump(tag)

    def put(self, name: str):
        tag_json = request.get_json()
        tag = TagModel.find_by_name(name)
        if tag:
            tag.title = tag_json["title"]
            tag.color = tag_json["color"]
        else:
            tag_json["name"] = name
            tag = tag_schema.load(tag_json)
        tag.save_to_db()
        return tag_schema.dump(tag)

    def delete(self, name: str):
        tag = TagModel.find_by_name(name)
        if tag:
            tag.delete_from_db()
            return {"message": f"deleted tag <tag={tag}>"}
        return {"message": "ERROR: Couldn't delete from database"}

class TagList(Resource):
    def get(self):
        return {"content": tag_list_schema.dump(TagModel.find_all())}