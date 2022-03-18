from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse
import os
from dotenv import load_dotenv

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL_SEM = "mysql+mysqlconnector://tha:dollars@localhost/test"

engine = create_engine(SQLALCHEMY_DATABASE_URL_SEM)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
