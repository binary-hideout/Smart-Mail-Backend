from ma import ma
from models.contact import ContactModel
from schemas.case import CaseSchema


class ContactSchema(ma.SQLAlchemyAutoSchema):
    cases = ma.Nested(CaseSchema, many=True)

    class Meta:
        model = ContactModel
        load_only = ("contact",)
        dump_only = (
            "id",
            "created",
        )
        include_fk = True
        load_instance = True
