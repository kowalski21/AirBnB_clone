#!/usr/bin/python3
import os
import unittest
from datetime import datetime, timedelta
from models.city import City
from time import sleep


class TestCityInstantiation(unittest.TestCase):
    def test_create_city_instance(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_id_type(self):
        city = City()
        self.assertIsInstance(city.id, str)

    def test_city_created_at_type(self):
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_city_updated_at_type(self):
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_name_type(self):
        city = City()
        self.assertIsInstance(city.name, str)

    def test_city_state_id_type(self):
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_city_id_uniqueness(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)


class TestCitySave(unittest.TestCase):
    def setUp(self):
        if os.path.exists("file.json"):
            os.rename("file.json", "file_backup.json")

    def tearDown(self):
        if os.path.exists("file_backup.json"):
            os.rename("file_backup.json", "file.json")

    def test_city_save(self):
        city = City()
        initial_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(initial_updated_at, city.updated_at)


class TestCityToDict(unittest.TestCase):
    def test_city_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["id"], city.id)
        self.assertEqual(city_dict["created_at"], city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], city.updated_at.isoformat())
        self.assertEqual(city_dict["__class__"], "City")


if __name__ == "__main__":
    unittest.main()
