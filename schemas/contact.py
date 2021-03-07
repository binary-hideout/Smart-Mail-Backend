from ma import ma
from models.contact import ContactModel

class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContactModel
        dump_only = ("id", "created",)
        load_instance = True