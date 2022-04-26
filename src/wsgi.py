from flask import g
from app import application
from src.db.entity.register import migrate


@application.before_request
def add_user_details():
    g.user_id = "admin"


if __name__ == "__main__":
    migrate()
    application.run(host='0.0.0.0', port=7000, debug=True)
