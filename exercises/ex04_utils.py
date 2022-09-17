"""EX04 - List Utility Functions."""
__author__ = "730560667"


def all(a: list[int], b: int) -> bool:
    """Test whether or not all of the ints in a list are the same as a given int."""
    if len(a) == 0:
        return False
    i: int = 0
    while i < len(a):
        if a[i] != b:
            return False
        i = i + 1
    return True


def max(input: list[int]) -> int:
    """Return the largest int in a list of ints."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_entry: int = input[0]
    i: int = 1
    while i < len(input):
        if max_entry < input[i]:
            max_entry = input[i]
        i = i + 1
    return max_entry


def is_equal(c: list[int], d: list[int]) -> bool:
    """Given two lists of int values, test if every element at every index is equal in both lists."""
    if len(c) != len(d):
        return False
    i: int = 0
    while i < len(c):
        if c[i] != d[i]:
            return False
        i = i + 1
    return True