"""Testing Dictionary Functions."""
__author__ = "730560667"


from dictionary import invert, favorite_color, count
import pytest


def test_invert_duplicate_keys() -> None:
    """Raise a KeyError for dupliate keys."""
    with pytest.raises(KeyError):
        original = {"kris": "jordan", "michael": "jordan"}
        invert(original)

    
def test_invert_empty_dictionary() -> None:
    """Return an empty dictionary if the input is an empty dictionary."""
    original: dict[str, str] = {}
    assert invert(original) == {}


def test_invert_use_case_one() -> None:
    """A working example of the invert function."""
    original = {"a": "first", "b": "second", "c": "third"}
    assert invert(original) == {"first": "a", "second": "b", "third": "c"}


def test_invert_use_case_two() -> None:
    """Another working example of the invert function."""
    original = {"duke": "ew", "unc": "slay"}
    assert invert(original) == {"ew": "duke", "slay": "unc"}


def test_favorite_color_empty_dictionary() -> None:
    """Return an empty dictionary if the input is an empty dictionary."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_use_case_one() -> None:
    """A working example of the favorite_color function."""
    colors = {"carsen": "blue", "timothy": "green", "sharkey": "green"}
    assert favorite_color(colors) == "green"


def test_favorite_color_use_case_two() -> None:
    """Another working example of the favorite_color function."""
    colors = {"paul": "red", "bill": "orange", "john": "yellow", "dan": "red", "fred": "orange"}
    assert favorite_color(colors) == "red"


def test_count_empty_list() -> None:
    """Return an empty dictionary if the input is an empty list."""
    input_list: list[str] = []
    assert count(input_list) == {}


def test_count_use_case_one() -> None:
    """A working example of the count function."""
    input_list = ["a", "b", "a", "a", "c", "b"]
    assert count(input_list) == {"a": 3, "b": 2, "c": 1}


def test_count_use_case_two() -> None:
    """Another working example of the count function."""
    input_list = ["carsen", "carsen", "carsen", "john"]
    assert count(input_list) == {"carsen": 3, "john": 1}