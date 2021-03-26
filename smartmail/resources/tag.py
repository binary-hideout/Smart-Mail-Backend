from flask import request
from flask_restful import Resource
from smartmail.schemas.schemas import TagSchema
from smartmail.models.tag import TagModel
from marshmallow import ValidationError

tag_schema = TagSchema()
tag_list_schema = TagSchema(many=True)


class Tag(Resource):
    def get(self, title: str):
        tag = TagModel.find_by_title(title)
        if tag:
            return tag_schema.dump(tag), 200
        return {"message": f"ERROR: Couldn't find requested tag <title={title}>"}, 404

    def post(self, title: str):
        tag = TagModel.find_by_title(title)
        if tag:
            return {"message": f"ERROR: Tag already exists <title={title}>"}
        tag_json = request.get_json()
        tag_json["title"] = title
        try:
            tag = tag_schema.load(tag_json)
        except ValidationError as err:
            return err.message

        try:
            tag.save_to_db()
        except:
            return {"message": f"ERROR: Couldn't save to database"}, 500
        return tag_schema.dump(tag), 201

    def put(self, title: str):
        tag_json = request.get_json()
        tag = TagModel.find_by_title(title)
        if tag:
            tag.color = tag_json["color"]
        else:
            tag_json["title"] = title
            tag = tag_schema.load(tag_json)
        tag.save_to_db()
        return tag_schema.dump(tag), 200

    def delete(self, title: str):
        tag = TagModel.find_by_title(title)
        if tag:
            tag.delete_from_db()
            return {"message": f"deleted tag <title={title}>"}, 200
        return {"message": "ERROR: Couldn't delete from database"}, 404


class TagList(Resource):
    def get(self):
        return {"content": tag_list_schema.dump(TagModel.find_all())}, 200