#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of number and return its value."""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
