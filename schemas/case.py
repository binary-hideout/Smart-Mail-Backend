from ma import ma
from models.tag import TagModel
from models.case import CaseModel

class CaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CaseModel
        load_only = ("tag",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True