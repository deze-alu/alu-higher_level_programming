#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Reproduce the behaviour described by the given bytecode."""
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
