#!/usr/bin/python3
"""testing for BaseModel using uttitest"""
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """testing the base model class"""

    @classmethod
    def setUpClass(cls):
        """setup for the basemodel test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """tear down the class after testing"""
        del cls.base

    def tearDown(self):
        """tear down the test after testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing basemodel for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for basemodel for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing Basemodel for working methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """checking model if it is a type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(os.environ['HBNB_TYPE_STORAGE'] == 'db',
                     'BaseModel not mapped')
    def test_save_BaesModel(self):
        """checking for the save"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """checking for the dictionary"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
