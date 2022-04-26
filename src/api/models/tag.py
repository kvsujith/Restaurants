from flask_restx import fields
from api.namespaces import tag
from flask_restx.fields import MarshallingError, String

a_tag = tag.model(
    'Tag',
    {
        'name': fields.String(required=True),
        'type': fields.Integer(required=True),
    }
)


class EnumField(String):
    """
    Custom EnumField for maping the right enum value
    """
    def __init__(self, *args, **kwargs):
        super(EnumField, self).__init__(*args, **kwargs)

    def format(self, value):
        try:
            # return the value of the given TagType object
            return value.value
        except ValueError as ve:
            raise MarshallingError(ve)
