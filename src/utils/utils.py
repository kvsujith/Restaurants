import json
from datetime import datetime, timedelta

from flask_restx import marshal


def get_indian_time():
    return datetime.utcnow() + timedelta(hours=5, minutes=30)


def get_json_data(res, format_structure: dict): return marshal(res, format_structure)
