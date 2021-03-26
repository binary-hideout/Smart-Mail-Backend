from smartmail.apps.ma import ma
from smartmail.models.contact import ContactModel
from smartmail.models.tag import TagModel
from smartmail.models.case import CaseModel

class CaseSchema(ma.SQLAlchemyAutoSchema):
    contact = ma.Nested(lambda: ContactSchema(only=("id", "email", "phone")))
    tag = ma.Nested(lambda: TagSchema(only=("id", "title", "color")))

    class Meta:
        model = CaseModel
        dump_only = ("id", "created")
        include_fk = True
        load_instance = True

class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContactModel
        load_only = ("contact",)
        dump_only = (
            "id",
            "created",
        )
        include_fk = True
        load_instance = True


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TagModel
        load_only = ("tag",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True