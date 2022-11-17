from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

"""Doc"""
Base = declarative_base()
class State(Base):
    """Doc"""
    __tablename__ = 'state'
    id = Column(Integer, autoincrement=True,
             unique=True, nullable=False, 
             primary_key=True)
    name = Column(String(128), nullable=False)