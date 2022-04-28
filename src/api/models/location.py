from flask_restx import fields
from api.namespaces import location

location_model = location.model("Location", {
    "name": fields.String(required=True)
})
