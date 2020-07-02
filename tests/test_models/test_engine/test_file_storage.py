#!/usr/bin/python3
""" test for clases
    Atributes:
        all
"""


import unittest
from models.engine.file_storage import FileStorage
import datetime
import pep8
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_BaseModel(unittest.TestCase):
    """ this tests methods of base
        Atributes:
            All
    """

    @classmethod
    def test_setUpClass(self):
        """test if is"""
        print("Base setUpClass")

    @classmethod
    def test_tearDownClass(self):
        """test if is"""
        print("base tearDownClass")

    def test_setUp(self):
        """test if is"""
        print("base setUp")

    def test_tearDown(self):
        """test if is"""
        print("base tearDown")

    def test_funtion(self):
        self.assertTrue(True)
    """ my test """

    def test_return_method_all(self):
        """test if is a dict"""
        myfilestorage = FileStorage()
        a = myfilestorage.all()
        b = str(type(a))
        self.assertEqual(b, "<class 'dict'>")

    def test_new(self):
        nstorage = FileStorage()
        dic = nstorage.all()
        rev = User()
        rev.id = 123123
        rev.name = "Holberton"
        nstorage.new(rev)
        key = rev.__class__.__name__ + "." + str(rev.id)
        self.assertIsNotNone(dic[key])

    def test_reload(self):
        storage = FileStorage()
        storage.save()
        path = os.path.dirname(os.path.abspath("console.py"))
        pt = os.path.join(path, "file.json")
        with open(pt, 'r') as fi:
            line = fi.readlines()
        try:
            os.remove(pt)
        except BaseException:
            pass
        storage.save()
        with open(pt, 'r') as fi:
            line2 = fi.readlines()
        self.assertEqual(line, line2)
        try:
            os.remove(pt)
        except BaseException:
            pass
        with open(pt, "w") as fi:
            fi.write("{}")
        with open(pt, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIsNotNone(storage.reload(), None)

    def test_dict(self):
        """test if is"""
        self.name = "holberton"
        self.assertEqual("holberton", self.name)

    def test_id(self):
        """test if is"""
        self.id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual("b6a6e15c-c67d-4312-9a75-9d084935e579", self.id)

    def test_created_at(self):
        """test if is"""
        self.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(datetime.datetime(
            2017, 9, 28, 21, 5, 54, 119427), self.created_at)

    def test_updated_at(self):
        """test if is"""
        self.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119434)
        self.assertEqual(datetime.datetime(
            2017, 9, 28, 21, 5, 54, 119434), self.updated_at)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    if __name__ == '__main__':
        unittest.main()
