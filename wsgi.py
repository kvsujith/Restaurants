from flask import Flask
from src.db.register import migrate

app = Flask(__name__)


if __name__ == "__main__":
    migrate()
    app.run(debug=True)
