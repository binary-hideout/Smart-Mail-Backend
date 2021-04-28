from flask import request, make_response, render_template, redirect, url_for
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
            # return tag_schema.dump(tag), 200
            headers = {"Content-Type": "text-html"}
            return make_response(
                render_template("tag.html", result=tag_schema.dump(tag)),
                200,
                headers,
            )
        return {"message": f"ERROR: Couldn't find requested tag <title={title}>"}, 404

    def post(self, title: str):
        tag_data = request.form.copy()
        tag = TagModel.find_by_title(title)
        if tag:
            tag.color = tag_data["color"]
        else:
            tag_data["title"] = title
            tag = tag_schema.load(tag_data)
        tag.save_to_db()
        # return tag_schema.dump(tag), 200
        return redirect(url_for("tag", title=title))


class TagDelete(Resource):
    def get(self, title: str):
        tag = TagModel.find_by_title(title)
        if tag:
            tag.delete_from_db()
            # return {"message": f"deleted tag <title={title}>"}, 200
            return redirect(url_for("taglist"))
        return {"message": "ERROR: Couldn't delete from database"}, 404


class TagList(Resource):
    def get(self):
        # return {"content": tag_list_schema.dump(TagModel.find_all())}, 200
        headers = {"Content-Type": "text-html"}
        return make_response(
            render_template(
                "tags.html", results=tag_list_schema.dump(TagModel.find_all())
            ),
            200,
            headers,
        )

    def post(self):
        tag_data = request.form.copy()
        title = tag_data["title"]
        tag = TagModel.find_by_title(title)
        if tag:
            return {"message": f"ERROR: Tag already exists <title={title}>"}

        try:
            tag = tag_schema.load(tag_data)
        except ValidationError as err:
            return err.message

        try:
            tag.save_to_db()
        except:
            return {"message": f"ERROR: Couldn't save to database"}, 500
        return tag_schema.dump(tag), 201
