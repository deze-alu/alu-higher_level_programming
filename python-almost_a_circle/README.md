# Python - Almost a circle

A small class hierarchy bringing together inheritance, private attributes with
validation, serialization to JSON and unit testing.

## Package

| File | Description |
|------|-------------|
| `models/base.py` | Manages the id of every shape and their JSON representation |
| `models/rectangle.py` | A rectangle with a validated size and position |
| `models/square.py` | A square, a rectangle whose sides are equal |

## Tests

| File | Description |
|------|-------------|
| `tests/test_models/test_base.py` | Unittests for the Base class |
| `tests/test_models/test_rectangle.py` | Unittests for the Rectangle class |
| `tests/test_models/test_square.py` | Unittests for the Square class |

## Running the tests

    python3 -m unittest discover tests
