#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.review import Review
from models.amenity import Amenity


if getenv("HBNB_TYPE_STORAGE") == "db":

    class Place(BaseModel, Base):
        """ A place to stay """

        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        reviews = relationship(
                "Review",
                backref="place",
                cascade="all, delete")

        amenities = relationship(
                "Amenity",
                secondary='place_amenity',
                viewonly=False,
                back_populates="place_amenities")

        place_amenity = Table(
                'place_amenity',
                Base.metadata,
                Column(
                    "place_id",
                    String(60),
                    ForeignKey('places.id'),
                    primary_key=True,
                    nullable=False),
                Column(
                    "amenity_id",
                    String(60),
                    ForeignKey('amenities.id'),
                    primary_key=True,
                    nullable=False))

else:

    class Place(BaseModel):

        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            ''' Return all reviews '''
            rev_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    rev_list.append(review)
            return rev_list

        @property
        def amenities(self):
            """ Get/set2 linked Amenities. """
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if obj.__class__.__name__ == 'Amenity':
                amenity_ids.append(value.id)
            else:
                pass
