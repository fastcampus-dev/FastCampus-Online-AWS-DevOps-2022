from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://<user>:<password>@ch2-sample-db.cygqw3bcyhzy.ap-northeast-2.rds.amazonaws.com:3306/ch2_sample_db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()