from smartmail.apps.ma import ma
from marshmallow import fields
from smartmail.models.contact import ContactModel
from smartmail.models.tag import TagModel
from smartmail.models.case import CaseModel
from smartmail.models.user import UserModel


class CaseSchema(ma.SQLAlchemyAutoSchema):
    contact = ma.Nested(lambda: ContactSchema(only=("id", "email", "phone")))
    tag = ma.Nested(lambda: TagSchema(only=("id", "title")))

    class Meta:
        model = CaseModel
        dump_only = ("id", "created")
        include_fk = True
        load_instance = True

    csrf_token = fields.Str()


class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContactModel
        load_only = ("contact")
        dump_only = (
            "id",
            "created",
        )
        include_fk = True
        load_instance = True

    csrf_token = fields.Str()


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TagModel
        load_only = ("tag",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True

    csrf_token = fields.Str()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
        load_instance = True

    id = fields.Int()
    csrf_token = fields.Str()
    username = fields.Str(required=True)
    password = fields.Str(required=True)
