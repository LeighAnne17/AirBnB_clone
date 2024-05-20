#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up for the tests.
        """
        self.model = BaseModel()

    def test_initialization(self):
        """
        Test initialization of a BaseModel instance.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        """
        Test that each instance gets a unique UUID.
        """
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_save_method(self):
        """
        Test the save method of the BaseModel.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel.
        """
        string = str(self.model)
        expected = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(string, expected)


if __name__ == '__main__':
    unittest.main()

