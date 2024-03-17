#!/usr/bin/python3
"""A python gile that contains a class definition and an instance Base"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Attributes:

    inherits from Base

    links to the MySQL table cities

    class attribute id that represents a column \
    of an auto-generated, unique integer, can’t be \
    null and is a primary key

    class attribute name that represents a column of a string \
    with maximum 128 characters and can’t be null
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, foreign_key("states.id"), nullable=False)
