#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String


class Amenity(BaseModel, Base):
    """menity inherits from BaseModel and Base (respect the order)"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
