"""
    Polite Lib
    Dict Tools
    Helpers for handling dicts

"""
import glom


def key_exists(the_dict: dict, the_path: str) -> bool:
    """Check that a dict key exists in a dictionary, by the dictionary key path, using dot notation.
    :unit-test: test_dict_utils::test__key_exists
    """
    try:
        glom.glom(the_dict, the_path)
        return True
    except glom.core.PathAccessError:
        return False


def key_with_value(the_dict: dict, the_path: str):
    """Provide the value from a dictionary key if it exists, checking that it has a value that is
    not a None type.
    :unit-test: test_dict_utils::test__key_with_value
    """
    try:
        found = glom.glom(the_dict, the_path)
        if found:
            return found
        else:
            return False
    except glom.core.PathAccessError:
        return False


def drop_keys(the_dict: dict, the_keys: list) -> dict:
    """Drop the specified keys from a dict if they exist in the dictionary.
    :unit-test: test_dict_utils::test__drop_keys
    """
    new_dict = {}
    for index, values in the_dict.items():
        if index not in the_keys:
            new_dict[index] = values
    return new_dict


# End File: polite-lib/src/polite-lib/utils/dict_tools.py
