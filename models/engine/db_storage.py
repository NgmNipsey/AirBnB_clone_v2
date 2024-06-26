#!/usr/bin/python3
"""Creating a new engine: DBStorage"""
import os
from sqlalchemy import create_engine
from models.base_model import Base

class DBStorage:
    """Representing a new engine class"""
    __engine = None
    __session = None
    def __init__(self):
        """Initializes the new instances"""
        self.__engine = create_engine("mysql+mysldb://{}:{}@{}/{}"
                                        .format(os.environ.get('HBNB_MYSQL_USER'),
                                            os.environ.get('HBNB_MYSQL_PWD'),
                                            os.environ.get('HBNB_MYSQL_HOST'),
                                            os.environ.get('HBNB_MYSQL_DB'))
                                        pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == test:
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Queries the database"""
        if cls:
            results = self.__session.query(eval(cls)).all()
        else:
            results = sel.__session.query(User, State, City, Amenity, Place, Review).all()
        return {f"{type(obj).__name__}.{obj.id}":obj for obj in results}

