from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(".env")
DB_MOTOR = os.environ["DB_MOTOR"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOSTNAME = os.environ["DB_HOSTNAME"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


# DB_MOTOR + DB_USER +":"+DB_PASSWORD +"@" +DB_HOSTNAME +":" +DB_PORT +"/"+DB_NAME
DATABASE_URL = "{}{}:{}@{}:{}/{}".format(
    DB_MOTOR,
    DB_USER,
    DB_PASSWORD,
    DB_HOSTNAME,
    DB_PORT,
    DB_NAME)
print(DATABASE_URL)
#DATABASE_URL = "postgresql+psycopg2://postgres:password@127.0.0.1:5432/test"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# add the models here to create the tables on startup
# from models.direction_user_model import DirectionUser
#Base.metadata.add_all([DirectionUser.__table__, Table2.__table__])

