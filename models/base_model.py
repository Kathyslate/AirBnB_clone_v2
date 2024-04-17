#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from datetime import datetime, timedelta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models.engine.db_storage import DBStorage

Base = declarative_base()

class BaseModel:
    """This module defines a base class for all models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """This module defines a base class for all models"""
        self.id = kwargs.get('id', None)
        self.created_at = kwargs.get('created_at', datetime.utcnow())
        self.updated_at = kwargs.get('updated_at', datetime.utcnow())
        for key, value in kwargs.items():
            if key!= 'id' and key!= 'created_at' and key!= 'updated_at':
                setattr(self, key, value)

    def to_dict(self):
        """This module defines a base class for all models"""
        dictionary = self.__dict__
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def save(self):
        """This module defines a base class for all models"""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """This module defines a base class for all models"""
        models.storage.delete(self)

    def update(self, **kwargs):
        """This module defines a base class for all models"""
        for key, value in kwargs.items():
            if key!= 'id' and key!= 'created_at' and key!= 'updated_at':
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        models.storage.save()
