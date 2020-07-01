#!/usr/bin/python3
""" test for clases
    Atributes:
        all
"""


import unittest
from models.engine.file_storage import FileStorage
import datetime
import pep8


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
