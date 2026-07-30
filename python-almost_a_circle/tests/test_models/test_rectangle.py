#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Checks how a Rectangle is built."""

    def test_inherits_base(self):
        """A rectangle is a shape."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_two_arguments(self):
        """The size alone is enough to build a rectangle."""
        shape = Rectangle(10, 2)
        self.assertEqual((shape.width, shape.height), (10, 2))

    def test_position_defaults_to_zero(self):
        """A rectangle sits at the origin by default."""
        shape = Rectangle(10, 2)
        self.assertEqual((shape.x, shape.y), (0, 0))

    def test_position_is_kept(self):
        """The given position is stored."""
        shape = Rectangle(10, 2, 3, 4)
        self.assertEqual((shape.x, shape.y), (3, 4))

    def test_given_id(self):
        """The given id is stored."""
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_id_is_incremented(self):
        """Two rectangles hold consecutive ids."""
        first = Rectangle(1, 1)
        second = Rectangle(1, 1)
        self.assertEqual(second.id, first.id + 1)

    def test_width_is_private(self):
        """The width is not reachable by its plain name."""
        with self.assertRaises(AttributeError):
            Rectangle(1, 2).__width

    def test_height_is_private(self):
        """The height is not reachable by its plain name."""
        with self.assertRaises(AttributeError):
            Rectangle(1, 2).__height

    def test_no_argument(self):
        """A width and a height are required."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        """A height is required."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_arguments(self):
        """A sixth argument is refused."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangleWidth(unittest.TestCase):
    """Checks the validation of the width."""

    def test_string(self):
        """A string is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_float(self):
        """A float is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 2)

    def test_none(self):
        """A missing value is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_list(self):
        """A list is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 2)

    def test_dictionary(self):
        """A dictionary is refused."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({}, 2)

    def test_zero(self):
        """A width of zero is refused."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative(self):
        """A negative width is refused."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_setter_type(self):
        """The setter checks the type as well."""
        shape = Rectangle(1, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            shape.width = "1"

    def test_setter_value(self):
        """The setter checks the value as well."""
        shape = Rectangle(1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            shape.width = -10

    def test_setter_keeps_the_old_value(self):
        """A refused value leaves the width untouched."""
        shape = Rectangle(1, 2)
        try:
            shape.width = -10
        except ValueError:
            pass
        self.assertEqual(shape.width, 1)

    def test_width_before_height(self):
        """The width is checked before the height."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", "2")


class TestRectangleHeight(unittest.TestCase):
    """Checks the validation of the height."""

    def test_string(self):
        """A string is refused."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_float(self):
        """A float is refused."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.5)

    def test_none(self):
        """A missing value is refused."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_zero(self):
        """A height of zero is refused."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_negative(self):
        """A negative height is refused."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_setter_type(self):
        """The setter checks the type as well."""
        shape = Rectangle(1, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            shape.height = {}

    def test_setter_value(self):
        """The setter checks the value as well."""
        shape = Rectangle(1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            shape.height = 0

    def test_height_before_x(self):
        """The height is checked before the position."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2", "3")


class TestRectangleX(unittest.TestCase):
    """Checks the validation of the horizontal offset."""

    def test_string(self):
        """A string is refused."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")

    def test_dictionary(self):
        """A dictionary is refused."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_float(self):
        """A float is refused."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 1.5)

    def test_negative(self):
        """A negative offset is refused."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_zero_is_allowed(self):
        """An offset of zero is accepted."""
        self.assertEqual(Rectangle(10, 2, 0).x, 0)

    def test_setter(self):
        """The setter checks the value as well."""
        shape = Rectangle(1, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            shape.x = -1

    def test_x_before_y(self):
        """The horizontal offset is checked before the vertical one."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3", "4")


class TestRectangleY(unittest.TestCase):
    """Checks the validation of the vertical offset."""

    def test_string(self):
        """A string is refused."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_float(self):
        """A float is refused."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, 4.5)

    def test_negative(self):
        """A negative offset is refused."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_zero_is_allowed(self):
        """An offset of zero is accepted."""
        self.assertEqual(Rectangle(10, 2, 3, 0).y, 0)

    def test_setter(self):
        """The setter checks the value as well."""
        shape = Rectangle(1, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            shape.y = "4"


class TestRectangleArea(unittest.TestCase):
    """Checks the area method."""

    def test_small(self):
        """The area of a small rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_tall(self):
        """The area of a tall rectangle."""
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_with_id(self):
        """The position and the id do not change the area."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_one_by_one(self):
        """The smallest rectangle holds a single cell."""
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_after_update(self):
        """The area follows the new size."""
        shape = Rectangle(2, 2)
        shape.width = 5
        self.assertEqual(shape.area(), 10)

    def test_no_argument_needed(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Checks the display method."""

    def display(self, shape):
        """Returns what the given shape prints."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            shape.display()
        return buffer.getvalue()

    def test_square_shape(self):
        """A two by two rectangle prints two rows."""
        self.assertEqual(self.display(Rectangle(2, 2)), "##\n##\n")

    def test_wide(self):
        """A wide rectangle prints wide rows."""
        self.assertEqual(self.display(Rectangle(4, 1)), "####\n")

    def test_tall(self):
        """A tall rectangle prints many rows."""
        self.assertEqual(self.display(Rectangle(1, 3)), "#\n#\n#\n")

    def test_one_by_one(self):
        """The smallest rectangle prints a single character."""
        self.assertEqual(self.display(Rectangle(1, 1)), "#\n")

    def test_horizontal_offset(self):
        """The horizontal offset adds spaces before each row."""
        self.assertEqual(self.display(Rectangle(2, 1, 3)), "   ##\n")

    def test_vertical_offset(self):
        """The vertical offset adds empty lines before the rows."""
        self.assertEqual(self.display(Rectangle(2, 1, 0, 2)), "\n\n##\n")

    def test_both_offsets(self):
        """Both offsets are taken into account."""
        self.assertEqual(self.display(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_returns_nothing(self):
        """The method returns nothing."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.assertIsNone(Rectangle(1, 1).display())


class TestRectangleStr(unittest.TestCase):
    """Checks the string representation."""

    def test_full(self):
        """Every attribute shows up in the description."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_default_position(self):
        """A missing offset shows up as a zero."""
        self.assertEqual(str(Rectangle(5, 5, 1, 0, 7)),
                         "[Rectangle] (7) 1/0 - 5/5")

    def test_print(self):
        """Printing a rectangle uses the same description."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print(Rectangle(1, 2, 3, 4, 5))
        self.assertEqual(buffer.getvalue(), "[Rectangle] (5) 3/4 - 1/2\n")

    def test_changes_with_the_attributes(self):
        """The description follows the new values."""
        shape = Rectangle(1, 2, 3, 4, 5)
        shape.width = 9
        self.assertEqual(str(shape), "[Rectangle] (5) 3/4 - 9/2")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Checks the update method with positional arguments."""

    def setUp(self):
        """Builds the rectangle used by the tests."""
        self.shape = Rectangle(10, 10, 10, 10, 1)

    def test_no_argument(self):
        """Nothing changes without an argument."""
        self.shape.update()
        self.assertEqual(str(self.shape), "[Rectangle] (1) 10/10 - 10/10")

    def test_id(self):
        """The first argument is the id."""
        self.shape.update(89)
        self.assertEqual(str(self.shape), "[Rectangle] (89) 10/10 - 10/10")

    def test_width(self):
        """The second argument is the width."""
        self.shape.update(89, 2)
        self.assertEqual(str(self.shape), "[Rectangle] (89) 10/10 - 2/10")

    def test_height(self):
        """The third argument is the height."""
        self.shape.update(89, 2, 3)
        self.assertEqual(str(self.shape), "[Rectangle] (89) 10/10 - 2/3")

    def test_x(self):
        """The fourth argument is the horizontal offset."""
        self.shape.update(89, 2, 3, 4)
        self.assertEqual(str(self.shape), "[Rectangle] (89) 4/10 - 2/3")

    def test_y(self):
        """The fifth argument is the vertical offset."""
        self.shape.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.shape), "[Rectangle] (89) 4/5 - 2/3")

    def test_extra_arguments_are_ignored(self):
        """A sixth argument matches no attribute."""
        self.shape.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(self.shape), "[Rectangle] (89) 4/5 - 2/3")

    def test_validation_still_applies(self):
        """A refused width still raises."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.shape.update(89, -2)

    def test_type_validation_still_applies(self):
        """A refused height still raises."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.shape.update(89, 2, "3")

    def test_id_is_not_validated(self):
        """The id accepts any value."""
        self.shape.update("holberton")
        self.assertEqual(self.shape.id, "holberton")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Checks the update method with keyword arguments."""

    def setUp(self):
        """Builds the rectangle used by the tests."""
        self.shape = Rectangle(10, 10, 10, 10, 1)

    def test_one_attribute(self):
        """A single keyword changes a single attribute."""
        self.shape.update(height=1)
        self.assertEqual(str(self.shape), "[Rectangle] (1) 10/10 - 10/1")

    def test_two_attributes(self):
        """Several keywords change several attributes."""
        self.shape.update(width=1, x=2)
        self.assertEqual(str(self.shape), "[Rectangle] (1) 2/10 - 1/10")

    def test_order_does_not_matter(self):
        """The order of the keywords changes nothing."""
        self.shape.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.shape), "[Rectangle] (89) 3/1 - 2/10")

    def test_every_attribute(self):
        """Every attribute can be given at once."""
        self.shape.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(str(self.shape), "[Rectangle] (1) 4/5 - 2/3")

    def test_unknown_keyword_is_added(self):
        """An unknown keyword becomes a new attribute."""
        self.shape.update(colour="red")
        self.assertEqual(self.shape.colour, "red")

    def test_args_wins_over_kwargs(self):
        """The keywords are skipped when positional values are given."""
        self.shape.update(89, 2, height=99)
        self.assertEqual(str(self.shape), "[Rectangle] (89) 10/10 - 2/10")

    def test_validation_still_applies(self):
        """A refused value still raises."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.shape.update(width="1")

    def test_empty_call(self):
        """Nothing changes without any value."""
        self.shape.update(**{})
        self.assertEqual(str(self.shape), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangleToDictionary(unittest.TestCase):
    """Checks the to_dictionary method."""

    def test_returns_a_dictionary(self):
        """The result is a dictionary."""
        self.assertIs(type(Rectangle(1, 2).to_dictionary()), dict)

    def test_keys(self):
        """Every attribute shows up as a key."""
        self.assertEqual(sorted(Rectangle(1, 2).to_dictionary().keys()),
                         ["height", "id", "width", "x", "y"])

    def test_values(self):
        """Every value is the one of the rectangle."""
        self.assertEqual(Rectangle(10, 2, 1, 9, 1).to_dictionary(),
                         {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_feeds_update(self):
        """The description can be applied to another rectangle."""
        original = Rectangle(10, 2, 1, 9, 1)
        copy = Rectangle(1, 1)
        copy.update(**original.to_dictionary())
        self.assertEqual(str(copy), str(original))

    def test_copy_is_a_new_object(self):
        """A rectangle built out of a description is a new object."""
        original = Rectangle(10, 2, 1, 9, 1)
        copy = Rectangle(1, 1)
        copy.update(**original.to_dictionary())
        self.assertIsNot(copy, original)

    def test_no_argument_needed(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
