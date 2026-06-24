#!/usr/bin/python3
def uppercase(str):
    """Print str in uppercase followed by a new line."""
    for c in str:
        n = ord(c)
        if ord("a") <= n <= ord("z"):
            n -= 32
        print("{}".format(chr(n)), end="")
    print("")
