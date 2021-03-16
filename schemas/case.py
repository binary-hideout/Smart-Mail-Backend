from ma import ma
from models.case import CaseModel


class CaseSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = CaseModel
        dump_only = ("id", "created")
        include_fk = True
        load_instance = True
