"""
    Convert
    File conversion tools    

"""
import json


def dict_to_json(python_data: dict, file_to_write: str) -> bool:
    """Convert a python dictionary to a json file."""
    if not python_data:
        return False
    data = json.dumps(python_data)
    with open(file_to_write, mode='w') as f:
        f.write(data)
    return True


# End File: polite-lib/src/polite-lib/file_tools/convert.py
