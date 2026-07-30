# Python - Test-driven development

Writing functions alongside the tests that describe them, with doctest files
for the interactive tests and the `unittest` module for the last task.

## Tasks

| File | Description |
|------|-------------|
| `0-add_integer.py` | Adds two integers |
| `2-matrix_divided.py` | Divides all the elements of a matrix |
| `3-say_my_name.py` | Prints a first name followed by a last name |
| `4-print_square.py` | Prints a square with the character # |
| `5-text_indentation.py` | Prints a text with two new lines after ., ? and : |
| `tests/6-max_integer_test.py` | Unittests for the max_integer function |

## Running the tests

    python3 -m doctest ./tests/*.txt
    python3 -m unittest tests.6-max_integer_test
