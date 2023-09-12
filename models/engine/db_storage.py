#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import MetaData, create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Manages storage of HBNB models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Starting the engine """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method that queries on the currect database session """
        objects = {}

        if cls is None:
            clasess = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

            for class_name in clasess:
                class_obj = getattr(models, class_name)
                all_objects = self.__session.query(class_obj).all()
                objects_dict = {
                        f"{class_name}.{obj.id}": obj for obj in all_objects}

                objects.update(objects_dict)

        else:
            class_cls = self.__session.query(cls).all()
            objects = {
                    f"{type(obj).__name__}.{obj.id}": obj for obj in class_cls}

        return objects

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reload all tables in the database and create a new session """
        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()
