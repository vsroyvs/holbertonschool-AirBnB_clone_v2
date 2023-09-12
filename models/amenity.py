#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':

    class Amenity(BaseModel, Base):
        """ class Amenity for connect to database """

        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)

        place_amenities = relationship(
                "Place",
                secondary='place_amenity',
                back_populates="amenities")

else:
    class Amenity(BaseModel):

        name = ""
