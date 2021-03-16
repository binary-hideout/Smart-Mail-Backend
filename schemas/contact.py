from ma import ma
from models.contact import ContactModel
from models.case import CaseModel
from schemas.case import CaseSchema


class ContactSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ContactModel
        load_only = ("contact",)
        dump_only = (
            "id",
            "created",
        )
        load_instance = True
