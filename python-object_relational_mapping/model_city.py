#!/usr/bin/python3
""" Doc """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


Base = declarative_base()
""" definition of a city and an instance Base = declarative_base(): """


class City(Base):
    """ class city inherits from Base """
    __tablename__ = 'city'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
