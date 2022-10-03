"""Unit tests for the functions in utils."""
__author__ = "730560667"


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Return an empty list given an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None:
    """Test that the function works with negative integers."""
    xs: list[int] = [-6, -4, -3, 2, 3, 6, 9, 10]
    assert only_evens(xs) == [-6, -4, 2, 6, 10]


def test_only_evens_many_items_again() -> None:
    """Basic use case with positive integers."""
    xs: list[int] = [4, 6, 1, 8, 5, 9, 2, 3, 3, 12]
    assert only_evens(xs) == [4, 6, 8, 2, 12]


def test_concat_empty() -> None:
    """Return an empty list given two empty input lists."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_concat_many_items() -> None:
    """One multiple int list and one empty list."""
    list_one: list[int] = [1, 3, 6, 2, 9]
    list_two: list[int] = []
    assert concat(list_one, list_two) == [1, 3, 6, 2, 9]


def test_concat_many_items_again() -> None:
    """Two multiple int lists."""
    list_one: list[int] = [1, 2, 3, 4, 5]
    list_two: list[int] = [6, 7, 8, 9, 10]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_sub_empty() -> None:
    """Return an empty list given an empty list."""
    xs: list[int] = []
    start = 1
    end = 3
    assert sub(xs, start, end) == []


def test_sub_negative_start() -> None:
    """Begin at the first entry of the list if the input start index is negative."""
    xs: list[int] = [3, 6, 9, 0, 4, 2]
    start = -3
    end = 4
    assert sub(xs, start, end) == [3, 6, 9, 0]


def test_sub_large_end_index() -> None:
    """End with the end of the list if the end index is greater than the length of the list."""
    xs: list[int] = [1, 2, 3]
    start = 0
    end = 5
    assert sub(xs, start, end) == [1, 2, 3]


def test_sub_use_case() -> None:
    """Basic use case."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    start = 1
    end = 4
    assert sub(xs, start, end) == [2, 3, 4]


def test_sub_another_use_case() -> None:
    """Another basic use case."""
    xs: list[int] = [1, 3, 5, 7, 9]
    start = 3
    end = 4
    assert sub(xs, start, end) == [7]