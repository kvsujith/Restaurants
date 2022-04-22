from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql://root:user@localhost:3306/sample", echo=False)

Base = declarative_base()


class SessionData:
    def __init__(self):
        self.session = sessionmaker(bind=engine)

    def __del__(self):
        if self.session:
            self.session.close_all()
