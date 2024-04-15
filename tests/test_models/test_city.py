#!/usr/bin/python3
"""test for city"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """testing the class city"""

    @classmethod
    def setUpClass(cls):
        """set up for testing class city"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """tear down class after testing"""
        del cls.city

    def tearDown(self):
        """tear down test after testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """checking the model for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """checking for docstrings works"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """checking if City has any attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """checking if the City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """checking the attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.environ['HBNB_TYPE_STORAGE'] == 'db',
                     'Invalid storage mode')
    def test_save_City(self):
        """checking for save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """checking for dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
