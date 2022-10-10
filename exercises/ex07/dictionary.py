"""Implementing Dictionary Functions."""
__author__ = "730560667"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, return a dictionary that inverts the keys and the values."""
    inverted: dict[str,str] = {}
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
    i: int = 0
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

def count(xs: list[str]) -> dict[str, int]:
    frequencies: dict[str, int] = {}
    i: int = 0
    while i < len(xs):
        if xs[i] in frequencies:
            frequencies[xs[i]] += 1
        else:
            frequencies[xs[i]] = 1
        i += 1
    return frequencies
