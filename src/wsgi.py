from flask import Flask
from src.db.entity.register import migrate

from app import application

if __name__ == "__main__":
    migrate()
    application.run(host='0.0.0.0', port=7000, debug=True)
