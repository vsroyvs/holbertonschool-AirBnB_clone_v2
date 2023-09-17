#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':

    class State(BaseModel, Base):
        """Class State for a MySQL db"""

        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
else:

    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            from models.city import City
            new_list_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    new_list_cities.append(city)
            return new_list_cities
