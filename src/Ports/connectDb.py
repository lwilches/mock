from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///FakeCtrol.sqlite')
Session = sessionmaker(bind=Engine)
Base = declarative_base()