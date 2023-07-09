#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session

"""This module defines a class to manage database storage for hbnb clone"""

hbnb_env = getenv("HBNB_ENV")
Base = declarative_base()


class DBStorage:
    """A class for managing storage of hbnb models in a database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new DBStorage instance"""
        mysql_user = os.getenv('HBNB_MYSQL_USER')
        mysql_password = os.getenv('HBNB_MYSQL_PWD')
        mysql_host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        mysql_db = os.getenv('HBNB_MYSQL_DB')

        db_url = f'mysql+mysqldb://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if hbnb_env == 'test':
            self.__drop_all_tables()

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        query_classes = [User, State, City, Amenity, Place, Review]

        if cls:
            if cls in query_classes:
                query_classes = [cls]
            else:
                return {}
        objects = {}
        for query_class in query_classes:
            results = self.__session.query(query_class).all()
            for obj in results:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates tables in the database and creates the current database session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))
        self.__session = Session()
