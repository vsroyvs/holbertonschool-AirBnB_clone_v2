#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':

    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'

        places = relationship("Place", backref="cities", cascade="all, delete")

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
else:

    class City(BaseModel):
        name = ''
        state_id = ''
