from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'mongodb+srv://lbizimungu:S9kmYKTmunyDNjNM@cluster0.gaeuej0.mongodb.net/'

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
