"""Dictionary related utility functions."""

__author__ = "730560667"

# Define your functions below

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] =[]
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
    """View the first N rows of a column-based table"""
    result: dict[str, list[str]] = {}
    for column in column_table:
        smaller_list: list = []
        for i in range(N):
            smaller_list.append(column[i])
        result[column] = smaller_list
    return result
        

