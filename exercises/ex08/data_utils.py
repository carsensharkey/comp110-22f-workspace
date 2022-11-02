"""Dictionary related utility functions."""


__author__ = "730560667"


# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """View the first N rows of a column-based table."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        smaller_list: list[str] = []
        if N >= len(column_table[column]):
            result = column_table
            return result
        else:
            for i in range(N):
                smaller_list.append(column_table[column][i])
            result[column] = smaller_list
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for name in column_names:
        result[name] = column_table[name]
    return result


def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in column_table_one:
        result[column] = column_table_one[column]
    for column in column_table_two:
        if column in result:
            result[column] += column_table_two[column]
        else:
            result[column] = column_table_two[column]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Given a list of strings, produce a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    count: dict[str, int] = {}
    for variable in input_list:
        if variable in count:
            count[variable] += 1
        else:
            count[variable] = 1
    return count