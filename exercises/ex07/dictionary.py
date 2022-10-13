"""Implementing Dictionary Functions."""
__author__ = "730560667"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, return a dictionary that inverts the keys and the values."""
    inverted: dict[str, str] = {}
    for key in original:
        if original[key] in inverted:
            raise KeyError("Cannot have duplicate keys in a dictionary.")
        inverted[original[key]] = key
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Given a dictionary of names and favorite colors, return the color that appears most frequently."""
    greatest_frequency: int = 0
    most_popular_color: str = ""
    frequencies: dict[str, int] = {}
    for name in colors:
        if colors[name] in frequencies:
            frequencies[colors[name]] += 1
        else:
            frequencies[colors[name]] = 1
    for color in frequencies:
        if frequencies[color] > greatest_frequency:
            greatest_frequency = frequencies[color]
            most_popular_color = color
    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """Given a list of strings, produce a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    count: dict[str, int] = {}
    i: int = 0
    while i < len(input_list):
        if input_list[i] in count:
            count[input_list[i]] += 1
        else:
            count[input_list[i]] = 1
        i += 1
    return count