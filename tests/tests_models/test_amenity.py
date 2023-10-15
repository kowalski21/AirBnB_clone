#!/usr/bin/python3
#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_init(unittest.TestCase):
    """Unittests for  instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        instance = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", instance.__dict__)

    def test_two_amenities_unique_ids(self):
        instance = Amenity()
        instance_2 = Amenity()
        self.assertNotEqual(instance.id, instance_2.id)

    def test_two_amenities_different_created_at(self):
        instance = Amenity()
        sleep(0.05)
        instance_2 = Amenity()
        self.assertLess(instance.created_at, instance_2.created_at)

    def test_two_amenities_different_updated_at(self):
        instance = Amenity()
        sleep(2.8)
        instance_2 = Amenity()
        self.assertLess(instance.updated_at, instance_2.updated_at)

    def test_str_reps(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        instance = Amenity()
        instance.id = "123456"
        instance.created_at = instance.updated_at = dt
        am_str = instance.__str__()
        self.assertIn("[Amenity] (123456)", am_str)
        self.assertIn("'id': '123456'", am_str)
        self.assertIn("'created_at': " + dt_repr, am_str)
        self.assertIn("'updated_at': " + dt_repr, am_str)

    def test_unused_arguments(self):
        instance = Amenity(None)
        self.assertNotIn(None, instance.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        instance = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(instance.id, "345")
        self.assertEqual(instance.created_at, dt)
        self.assertEqual(instance.updated_at, dt)

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save_instance(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test__only_one_save(self):
        instance = Amenity()
        sleep(0.5)
        first_updated_at = instance.updated_at
        instance.save()
        self.assertLess(first_updated_at, instance.updated_at)

    def test_only_two_saves(self):
        am = Amenity()
        sleep(4)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_with_attributes(self):
        am = Amenity()
        am.middle_name = "Airbnb"
        am.my_number = 106
        self.assertEqual("Airbnb", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "Amenity",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_other_dict_info(self):
        instance = Amenity()
        self.assertNotEqual(instance.to_dict(), instance.__dict__)

    def test_to_dict_with_arg(self):
        instance = Amenity()
        with self.assertRaises(TypeError):
            instance.to_dict(None)


if __name__ == "__main__":
    unittest.main()
