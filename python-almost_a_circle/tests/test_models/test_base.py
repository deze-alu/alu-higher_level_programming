#!/usr/bin/python3
"""Unittests for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseId(unittest.TestCase):
    """Checks how the id of a Base is assigned."""

    def test_id_is_incremented(self):
        """Two shapes created in a row hold consecutive ids."""
        first = Base()
        second = Base()
        self.assertEqual(second.id, first.id + 1)

    def test_given_id_is_kept(self):
        """A given id is used as it is."""
        self.assertEqual(Base(89).id, 89)

    def test_given_id_does_not_increment(self):
        """A given id leaves the counter untouched."""
        before = Base()
        Base(89)
        after = Base()
        self.assertEqual(after.id, before.id + 1)

    def test_id_none(self):
        """A None id falls back to the counter."""
        self.assertIsNotNone(Base(None).id)

    def test_id_zero(self):
        """Zero is a value like any other."""
        self.assertEqual(Base(0).id, 0)

    def test_id_negative(self):
        """A negative id is kept as it is."""
        self.assertEqual(Base(-7).id, -7)

    def test_id_string(self):
        """The type of the id is not checked."""
        self.assertEqual(Base("holberton").id, "holberton")

    def test_nb_objects_is_private(self):
        """The counter is not reachable by its plain name."""
        with self.assertRaises(AttributeError):
            Base().__nb_objects

    def test_too_many_arguments(self):
        """A second positional argument is refused."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Checks the to_json_string static method."""

    def test_none(self):
        """A None list gives an empty JSON list."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list gives an empty JSON list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_returns_a_string(self):
        """The result is always a string."""
        self.assertIs(type(Base.to_json_string([{"id": 1}])), str)

    def test_one_dictionary(self):
        """A single dictionary is serialized."""
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_two_dictionaries(self):
        """Every dictionary of the list is kept."""
        given = [{"id": 1}, {"id": 2}]
        self.assertEqual(json.loads(Base.to_json_string(given)), given)

    def test_full_rectangle_dictionary(self):
        """A whole rectangle description survives the trip."""
        given = [Rectangle(10, 7, 2, 8, 1).to_dictionary()]
        self.assertEqual(json.loads(Base.to_json_string(given)), given)

    def test_no_argument(self):
        """The list is required."""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestBaseFromJsonString(unittest.TestCase):
    """Checks the from_json_string static method."""

    def test_none(self):
        """A None string gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_empty_json_list(self):
        """An empty JSON list gives an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_returns_a_list(self):
        """The result is always a list."""
        self.assertIs(type(Base.from_json_string('[{"id": 1}]')), list)

    def test_holds_dictionaries(self):
        """The list holds dictionaries."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertIs(type(result[0]), dict)

    def test_round_trip(self):
        """A list serialized and read back is unchanged."""
        given = [{"id": 89, "width": 10, "height": 4}]
        self.assertEqual(Base.from_json_string(Base.to_json_string(given)),
                         given)

    def test_invalid_json(self):
        """A malformed string is refused."""
        with self.assertRaises(ValueError):
            Base.from_json_string("{not json}")

    def test_no_argument(self):
        """The string is required."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBaseSaveToFile(unittest.TestCase):
    """Checks the save_to_file class method."""

    def tearDown(self):
        """Removes the files written by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            try:
                os.remove(name)
            except FileNotFoundError:
                pass

    def test_file_is_created(self):
        """A file named after the class shows up."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_square_file_name(self):
        """The file of a square carries the name of its class."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_none(self):
        """A None list writes an empty JSON list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_empty_list(self):
        """An empty list writes an empty JSON list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_content(self):
        """The file holds the description of every shape."""
        shape = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([shape])
        with open("Rectangle.json") as a_file:
            self.assertEqual(json.loads(a_file.read()),
                             [shape.to_dictionary()])

    def test_two_shapes(self):
        """Every shape of the list is written."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        with open("Rectangle.json") as a_file:
            self.assertEqual(len(json.loads(a_file.read())), 2)

    def test_overwrites(self):
        """A second call replaces the content of the file."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6)])
        with open("Rectangle.json") as a_file:
            self.assertEqual(len(json.loads(a_file.read())), 1)

    def test_returns_nothing(self):
        """The method returns nothing."""
        self.assertIsNone(Rectangle.save_to_file([]))

    def test_no_argument(self):
        """The list is required."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBaseCreate(unittest.TestCase):
    """Checks the create class method."""

    def test_rectangle_attributes(self):
        """Every attribute of the description is applied."""
        given = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        shape = Rectangle.create(**given)
        self.assertEqual(shape.to_dictionary(), given)

    def test_square_attributes(self):
        """A square is built out of its own description."""
        given = {"id": 89, "size": 1, "x": 2, "y": 3}
        shape = Square.create(**given)
        self.assertEqual(shape.to_dictionary(), given)

    def test_returns_the_right_class(self):
        """The built shape belongs to the calling class."""
        self.assertIs(type(Rectangle.create(**{"width": 1, "height": 2})),
                      Rectangle)

    def test_square_returns_a_square(self):
        """A square is built when the square class calls the method."""
        self.assertIs(type(Square.create(**{"size": 1})), Square)

    def test_is_a_new_object(self):
        """The built shape is not the one it was described by."""
        original = Rectangle(3, 5, 1)
        copy = Rectangle.create(**original.to_dictionary())
        self.assertIsNot(original, copy)

    def test_is_not_equal(self):
        """Two shapes holding the same values are still different."""
        original = Rectangle(3, 5, 1)
        copy = Rectangle.create(**original.to_dictionary())
        self.assertNotEqual(original, copy)

    def test_partial_dictionary(self):
        """A partial description leaves the other attributes alone."""
        self.assertEqual(Rectangle.create(**{"width": 7}).width, 7)

    def test_empty_dictionary(self):
        """An empty description gives the dummy shape."""
        self.assertIsNotNone(Rectangle.create())


class TestBaseLoadFromFile(unittest.TestCase):
    """Checks the load_from_file class method."""

    def tearDown(self):
        """Removes the files written by the tests."""
        for name in ("Rectangle.json", "Square.json"):
            try:
                os.remove(name)
            except FileNotFoundError:
                pass

    def test_missing_file(self):
        """A missing file gives an empty list."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_returns_a_list(self):
        """The result is a list."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertIs(type(Rectangle.load_from_file()), list)

    def test_number_of_shapes(self):
        """Every saved shape is read back."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        self.assertEqual(len(Rectangle.load_from_file()), 2)

    def test_rectangle_type(self):
        """The read shapes are rectangles."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertIs(type(Rectangle.load_from_file()[0]), Rectangle)

    def test_square_type(self):
        """The read shapes are squares."""
        Square.save_to_file([Square(1)])
        self.assertIs(type(Square.load_from_file()[0]), Square)

    def test_values_are_kept(self):
        """A shape read back holds the values it was saved with."""
        shape = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([shape])
        self.assertEqual(str(Rectangle.load_from_file()[0]), str(shape))

    def test_square_values_are_kept(self):
        """A square read back holds the values it was saved with."""
        shape = Square(7, 9, 1, 5)
        Square.save_to_file([shape])
        self.assertEqual(str(Square.load_from_file()[0]), str(shape))

    def test_shapes_are_new_objects(self):
        """The read shapes are not the saved ones."""
        shape = Rectangle(1, 2)
        Rectangle.save_to_file([shape])
        self.assertIsNot(Rectangle.load_from_file()[0], shape)

    def test_empty_file(self):
        """A file holding an empty list gives an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
