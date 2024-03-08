"""
    Polite Lib
    Utils
    Format numbers

"""


def add_commas(value):
    """
    This function takes an integer or float value and returns a string with commas every 3 digits.
    Args:
        value: The integer or float value to format.
    Returns:
        A string with commas every 3 digits.
    """
    formatted_value = "{:,}".format(int(value))
    return formatted_value

# End File: polite-lib/src/polite-lib/utils/fmt_mumbers.py
