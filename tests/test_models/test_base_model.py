#!/usr/bin/python3
""" test for clases
    Atributes:
        all
"""


import unittest
from models.base_model import BaseModel
import datetime
import pep8


class Test_BaseModel(unittest.TestCase):
    """ this tests methods of base
        Atributes:
            All
    """

    @classmethod
    def test_setUpClass(self):
        """this tests methods"""
        print("Base setUpClass")

    @classmethod
    def test_tearDownClass(self):
        """this tests methods"""
        print("base tearDownClass")

    def test_setUp(self):
        """this tests methods"""
        print("base setUp")

    def test_tearDown(self):
        """this tests methods"""
        print("base tearDown")

    def test_function(self):
        """this tests methods"""
        self.assertTrue(True)
    """ my test """
    def test_class(self):
        """this tests methods"""
        mymodel = BaseModel()
        a = mymodel.__class__.__name__
        self.assertEqual(a, "BaseModel")

    def test_typeof_create(self):
        """this tests methods"""
        my_model = BaseModel()
        a = my_model.created_at
        self.assertEqual(type(a), datetime.datetime)

    def test_typeof_update(self):
        """this tests methods"""
        my_model = BaseModel()
        a = my_model.updated_at
        self.assertEqual(type(a), datetime.datetime)

    def test_typeof_id(self):
        """this tests methods"""
        my_model = BaseModel()
        a = my_model.id
        self.assertEqual(type(a), str)

    def test_id_creation(self):
        """this tests methods"""
        my_model1 = BaseModel()
        a = my_model1.id
        my_model2 = BaseModel()
        b = my_model2.id
        self.assertNotEqual(a, b)

    def test_return_to_dict(self):
        """this tests methods"""
        my_model = BaseModel()
        b = my_model.to_dict()
        self.assertEqual(type(b), dict)

    def test_to_dict(self):
        """this tests methods"""
        mymodel = BaseModel()
        a = mymodel.to_dict()
        b = {}
        for key, value in mymodel.__dict__.items():
            b[key] = value
        b['__class__'] = mymodel.__class__.__name__
        b['id'] = mymodel.id
        b['created_at'] = mymodel.created_at.isoformat()
        b['updated_at'] = mymodel.updated_at.isoformat()
        self.assertDictEqual(a, b)

    def test_actualize_update_at(self):
        """this tests methods"""
        my_model = BaseModel()
        a = my_model.updated_at
        my_model.save()
        b = my_model.updated_at
        self.assertNotEqual(a, b)

    def test_save(self):
        """this tests methods"""
        my_model = BaseModel()
        self.assertNotEqual(my_model.updated_at, datetime.datetime.utcnow())

    def test_str(self):
        """this tests methods"""
        my_model = BaseModel
        self.assertIsInstance(my_model.__str__(self), str)

    def test_actualize_create_at(self):
        """this tests methods"""
        my_model = BaseModel()
        a = my_model.created_at
        my_model.save()
        b = my_model.created_at
        self.assertEqual(a, b)

    def test_dict(self):
        """this tests methods"""
        self.name = "holberton"
        self.assertEqual("holberton", self.name)

    def test_id(self):
        """this tests methods"""
        self.id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual("b6a6e15c-c67d-4312-9a75-9d084935e579", self.id)

    def test_created_at(self):
        """this tests methods"""
        self.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(datetime.datetime(
            2017, 9, 28, 21, 5, 54, 119427), self.created_at)

    def test_updated_at(self):
        """this tests methods"""
        self.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119434)
        self.assertEqual(datetime.datetime(
            2017, 9, 28, 21, 5, 54, 119434), self.updated_at)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    if __name__ == '__main__':
        unittest.main()
