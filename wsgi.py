from flask import Flask
from src.db.BaseDB import Base, engine

app = Flask(__name__)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True)
