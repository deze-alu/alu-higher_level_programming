#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import json
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Checks how a Square is built."""

    def test_inherits_rectangle(self):
        """A square is a rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_inherits_base(self):
        """A square is a shape."""
        self.assertIsInstance(Square(1), Base)

    def test_size_feeds_both_sides(self):
        """The size becomes the width and the height."""
        shape = Square(5)
        self.assertEqual((shape.width, shape.height), (5, 5))

    def test_position_defaults_to_zero(self):
        """A square sits at the origin by default."""
        shape = Square(5)
        self.assertEqual((shape.x, shape.y), (0, 0))

    def test_horizontal_offset(self):
        """The second argument is the horizontal offset."""
        self.assertEqual(Square(2, 2).x, 2)

    def test_vertical_offset(self):
        """The third argument is the vertical offset."""
        self.assertEqual(Square(3, 1, 3).y, 3)

    def test_given_id(self):
        """The fourth argument is the id."""
        self.assertEqual(Square(1, 2, 3, 89).id, 89)

    def test_id_is_incremented(self):
        """Two squares hold consecutive ids."""
        first = Square(1)
        second = Square(1)
        self.assertEqual(second.id, first.id + 1)

    def test_no_new_attribute(self):
        """A square holds the attributes of a rectangle only."""
        self.assertEqual(sorted(Square(1).__dict__.keys()),
                         ["_Rectangle__height", "_Rectangle__width",
                          "_Rectangle__x", "_Rectangle__y", "id"])

    def test_no_argument(self):
        """A size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_arguments(self):
        """A fifth argument is refused."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquareSize(unittest.TestCase):
    """Checks the size getter and setter."""

    def test_getter(self):
        """The size is the width of the square."""
        self.assertEqual(Square(5).size, 5)

    def test_setter(self):
        """Setting the size changes both sides."""
        shape = Square(5)
        shape.size = 10
        self.assertEqual((shape.width, shape.height), (10, 10))

    def test_setter_changes_the_description(self):
        """The description follows the new size."""
        shape = Square(5, 0, 0, 1)
        shape.size = 10
        self.assertEqual(str(shape), "[Square] (1) 0/0 - 10")

    def test_string(self):
        """A string is refused with the message of the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("9")

    def test_setter_string(self):
        """The setter refuses a string as well."""
        shape = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            shape.size = "9"

    def test_float(self):
        """A float is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.5)

    def test_none(self):
        """A missing value is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_zero(self):
        """A size of zero is refused."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative(self):
        """A negative size is refused."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_setter_negative(self):
        """The setter refuses a negative size as well."""
        shape = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            shape.size = -1

    def test_refused_value_keeps_the_old_one(self):
        """A refused size leaves the square untouched."""
        shape = Square(5)
        try:
            shape.size = -1
        except ValueError:
            pass
        self.assertEqual(shape.size, 5)

    def test_offsets_are_still_validated(self):
        """The offsets keep their own messages."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_vertical_offset_string(self):
        """A vertical offset that is not an integer is refused."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_negative_horizontal_offset(self):
        """A negative horizontal offset is refused."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_negative_offset(self):
        """A negative offset is refused."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


class TestSquareArea(unittest.TestCase):
    """Checks the inherited area method."""

    def test_small(self):
        """The area of a small square."""
        self.assertEqual(Square(2).area(), 4)

    def test_bigger(self):
        """The area of a bigger square."""
        self.assertEqual(Square(5).area(), 25)

    def test_one(self):
        """The smallest square holds a single cell."""
        self.assertEqual(Square(1).area(), 1)

    def test_after_resize(self):
        """The area follows the new size."""
        shape = Square(2)
        shape.size = 7
        self.assertEqual(shape.area(), 49)


class TestSquareDisplay(unittest.TestCase):
    """Checks the inherited display method."""

    def display(self, shape):
        """Returns what the given shape prints."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            shape.display()
        return buffer.getvalue()

    def test_two(self):
        """A square of size two prints two rows."""
        self.assertEqual(self.display(Square(2)), "##\n##\n")

    def test_one(self):
        """A square of size one prints a single character."""
        self.assertEqual(self.display(Square(1)), "#\n")

    def test_horizontal_offset(self):
        """The horizontal offset adds spaces before each row."""
        self.assertEqual(self.display(Square(2, 2)), "  ##\n  ##\n")

    def test_vertical_offset(self):
        """The vertical offset adds empty lines before the rows."""
        self.assertEqual(self.display(Square(1, 0, 2)), "\n\n#\n")

    def test_both_offsets(self):
        """Both offsets are taken into account."""
        self.assertEqual(self.display(Square(3, 1, 3)),
                         "\n\n\n ###\n ###\n ###\n")


class TestSquareStr(unittest.TestCase):
    """Checks the string representation."""

    def test_full(self):
        """The size shows up once, not twice."""
        self.assertEqual(str(Square(5, 0, 0, 1)), "[Square] (1) 0/0 - 5")

    def test_with_offsets(self):
        """Both offsets show up in the description."""
        self.assertEqual(str(Square(3, 1, 3, 7)), "[Square] (7) 1/3 - 3")

    def test_print(self):
        """Printing a square uses the same description."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print(Square(2, 2, 0, 3))
        self.assertEqual(buffer.getvalue(), "[Square] (3) 2/0 - 2\n")

    def test_differs_from_rectangle(self):
        """A square does not describe itself as a rectangle."""
        self.assertNotIn("Rectangle", str(Square(1)))


class TestSquareUpdateArgs(unittest.TestCase):
    """Checks the update method with positional arguments."""

    def setUp(self):
        """Builds the square used by the tests."""
        self.shape = Square(5, 0, 0, 1)

    def test_no_argument(self):
        """Nothing changes without an argument."""
        self.shape.update()
        self.assertEqual(str(self.shape), "[Square] (1) 0/0 - 5")

    def test_id(self):
        """The first argument is the id."""
        self.shape.update(10)
        self.assertEqual(str(self.shape), "[Square] (10) 0/0 - 5")

    def test_size(self):
        """The second argument is the size."""
        self.shape.update(1, 2)
        self.assertEqual(str(self.shape), "[Square] (1) 0/0 - 2")

    def test_x(self):
        """The third argument is the horizontal offset."""
        self.shape.update(1, 2, 3)
        self.assertEqual(str(self.shape), "[Square] (1) 3/0 - 2")

    def test_y(self):
        """The fourth argument is the vertical offset."""
        self.shape.update(1, 2, 3, 4)
        self.assertEqual(str(self.shape), "[Square] (1) 3/4 - 2")

    def test_extra_arguments_are_ignored(self):
        """A fifth argument matches no attribute."""
        self.shape.update(1, 2, 3, 4, 5)
        self.assertEqual(str(self.shape), "[Square] (1) 3/4 - 2")

    def test_size_changes_both_sides(self):
        """Updating the size changes the width and the height."""
        self.shape.update(1, 7)
        self.assertEqual((self.shape.width, self.shape.height), (7, 7))

    def test_validation_still_applies(self):
        """A refused size still raises."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.shape.update(1, -2)


class TestSquareUpdateKwargs(unittest.TestCase):
    """Checks the update method with keyword arguments."""

    def setUp(self):
        """Builds the square used by the tests."""
        self.shape = Square(5, 0, 0, 1)

    def test_horizontal_offset(self):
        """A single keyword changes a single attribute."""
        self.shape.update(x=12)
        self.assertEqual(str(self.shape), "[Square] (1) 12/0 - 5")

    def test_size_and_offset(self):
        """Several keywords change several attributes."""
        self.shape.update(size=7, y=1)
        self.assertEqual(str(self.shape), "[Square] (1) 0/1 - 7")

    def test_with_id(self):
        """The id can be given as a keyword too."""
        self.shape.update(size=7, id=89, y=1)
        self.assertEqual(str(self.shape), "[Square] (89) 0/1 - 7")

    def test_order_does_not_matter(self):
        """The order of the keywords changes nothing."""
        self.shape.update(y=3, size=2, x=1)
        self.assertEqual(str(self.shape), "[Square] (1) 1/3 - 2")

    def test_args_wins_over_kwargs(self):
        """The keywords are skipped when positional values are given."""
        self.shape.update(89, 2, size=99)
        self.assertEqual(str(self.shape), "[Square] (89) 0/0 - 2")

    def test_validation_still_applies(self):
        """A refused value still raises."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.shape.update(size="7")


class TestSquareToDictionary(unittest.TestCase):
    """Checks the to_dictionary method."""

    def test_returns_a_dictionary(self):
        """The result is a dictionary."""
        self.assertIs(type(Square(1).to_dictionary()), dict)

    def test_keys(self):
        """The size shows up instead of the width and the height."""
        self.assertEqual(sorted(Square(1).to_dictionary().keys()),
                         ["id", "size", "x", "y"])

    def test_values(self):
        """Every value is the one of the square."""
        self.assertEqual(Square(10, 2, 1, 1).to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_no_width_key(self):
        """The width does not show up."""
        self.assertNotIn("width", Square(1).to_dictionary())

    def test_feeds_update(self):
        """The description can be applied to another square."""
        original = Square(10, 2, 1, 1)
        copy = Square(1, 1)
        copy.update(**original.to_dictionary())
        self.assertEqual(str(copy), str(original))

    def test_copy_is_a_new_object(self):
        """A square built out of a description is a new object."""
        original = Square(10, 2, 1, 1)
        copy = Square(1, 1)
        copy.update(**original.to_dictionary())
        self.assertIsNot(copy, original)


class TestSquareSaveToFile(unittest.TestCase):
    """Checks the inherited save_to_file class method."""

    def tearDown(self):
        """Removes the file written by the tests."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_none(self):
        """A None list writes an empty JSON list."""
        Square.save_to_file(None)
        with open("Square.json") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_empty_list(self):
        """An empty list writes an empty JSON list."""
        Square.save_to_file([])
        with open("Square.json") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_file_name(self):
        """The file carries the name of the class."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_content(self):
        """The file holds the description of the square."""
        shape = Square(10, 2, 1, 1)
        Square.save_to_file([shape])
        with open("Square.json") as a_file:
            self.assertEqual(json.loads(a_file.read()),
                             [shape.to_dictionary()])

    def test_two_squares(self):
        """Every square of the list is written."""
        Square.save_to_file([Square(1), Square(2)])
        with open("Square.json") as a_file:
            self.assertEqual(len(json.loads(a_file.read())), 2)

    def test_overwrites(self):
        """A second call replaces the content of the file."""
        Square.save_to_file([Square(1), Square(2)])
        Square.save_to_file([Square(3)])
        with open("Square.json") as a_file:
            self.assertEqual(len(json.loads(a_file.read())), 1)

    def test_returns_nothing(self):
        """The method returns nothing."""
        self.assertIsNone(Square.save_to_file([]))

    def test_round_trip(self):
        """A square saved and read back holds the same values."""
        shape = Square(7, 9, 1, 5)
        Square.save_to_file([shape])
        self.assertEqual(str(Square.load_from_file()[0]), str(shape))


if __name__ == "__main__":
    unittest.main()
