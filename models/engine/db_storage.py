#!/usr/bin/python3
"""storage engine when using MySQL database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import environ
from models.base_model import BaseModel

class DBStorage:
    """in class db_storage"""
    __engine = None
    __session = None

    def __init__(self):
        """in class db_storage"""
        self.__engine = create_engine(
            "mysql+mysqldb://{user}:{password}@{host}/{database}?unix_socket=/cloudsql/{socket}"
           .format(
                user=environ.get('HBNB_MYSQL_USER'),
                password=environ.get('HBNB_MYSQL_PWD'),
                host=environ.get('HBNB_MYSQL_HOST'),
                database=environ.get('HBNB_MYSQL_DB'),
                socket=environ.get('HBNB_MYSQL_SOCKET')
            ),
            pool_pre_ping=True
        )
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(expire_on_commit=False, bind=self.__engine))

    def all(self, cls=None):
        """in class db_storage"""
        if cls is None:
            return {x.__name__ + '.' + str(x.id): x for x in self.__session.query(Base).all()}
        else:
            return {x.id: x for x in self.__session.query(cls).all()}

    def new(self, obj):
        """in class db_storage"""
        self.__session.add(obj)

    def save(self):
        """in class db_storage"""
        self.__session.commit()

    def delete(self, obj=None):
        """in class db_storage"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """in class db_storage"""
        pass
