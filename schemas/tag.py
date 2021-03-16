from ma import ma
from models.tag import TagModel
from schemas.case import CaseSchema


class TagSchema(ma.SQLAlchemyAutoSchema):
    cases = ma.Nested(CaseSchema, many=True)

    class Meta:
        model = TagModel
        load_only = ("tag",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True

