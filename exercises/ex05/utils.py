"""Practice with list utility functions."""
__author__ = "730560667"

def only_evens(xs: list[int]) -> list[int]:
    """Given a list of ints, return a new list containing the even elements of the input list."""
    i: int = 0
    evens: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given two lists of ints, return a list containing the elements of the first list followed by the elements of the second list."""
    new_list: list[int] = []
    for item in list_one:
        new_list.append(item)
    for item in list_two:
        new_list.append(item)
    return new_list
    

def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Generate a list which is a subset of the given list between the specified start index (inclusive) and end index (exclusive)."""
    subset: list[int] = []
    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs) - 1
    if len(xs) == 0 or start > len(xs) or end <= 0:
        return []
    i = start
    while i < end:
        subset.append(xs[i])
        i += 1
    return subset
