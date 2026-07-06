#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return []
    return [number % 2 == 0 for number in my_list]
