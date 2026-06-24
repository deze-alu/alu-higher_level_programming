#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    print("{} argument{}{}".format(
        n,
        "" if n == 1 else "s",
        "." if n == 0 else ":"))
    for i in range(1, n + 1):
        print("{}: {}".format(i, argv[i]))
