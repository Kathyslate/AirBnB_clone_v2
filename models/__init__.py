#!/usr/bin/python3
"""Create a unique storage instance for your application"""
import os
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
