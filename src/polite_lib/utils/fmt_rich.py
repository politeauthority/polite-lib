"""
    Polite Lib
    Utils
    Format Rich
    This module helps working with the Rich Cli display module

"""
import logging

from rich.table import Table


def fmt_value(thing) -> str:
    """Rich tables do not like values that are not strings."""
    if thing == 0:
        return str(0)
    if not thing:
        return ""
    if not isinstance(thing, str):
        return str(thing)
    return thing


def key_value_table(data: dict, title: str = None):
    """
    """
    if not data:
        logging.warning("Rich Fmt helper given no data")
        return False
    table = Table(title=fmt_value(title))
    table.add_column("Key", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    for key, value in data.items():
        table.add_row(
            fmt_value(key),
            fmt_value(value))
    return table


def rows_table(rows: list, title: str = None):
    table = Table(title=fmt_value(title))
    columns = len(rows[0])
    for x in range(columns):
        if x != 0:
            table.add_column(justify="right")
        else:
            table.add_column("")
    data = []
    for row in rows:
        new_row = []
        for cell in row: 
            new_row.append(fmt_value(cell))
        data.append(new_row)
    for row in data:
        table.add_row(*row)
    return table

# End File: polite-lib/src/polite-lib/utils/fmt_rich.py
