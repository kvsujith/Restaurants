from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql://root:******@localhost:3306/sample", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()