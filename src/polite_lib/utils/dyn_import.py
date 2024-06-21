"""
    Polite Lib
    Utils
    Dynamic Import
        Tools for dynamically importing modules.

"""

import importlib.util


def get(module_name: str):
    """Dynamically import a module by it's string name."""
    module_filename = f"./{module_name}.py"
    module_spec = importlib.util.spec_from_file_location(module_name, module_filename)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def method(module, method_name: str):
    """Dynamically return a method if it exists."""
    if hasattr(module, method_name):
        method = getattr(module, method_name)
        return method()
    else:
        raise AttributeError(f"Method '{method_name}' not found in module '{module}'")


# End File: politeauthority/polite-lib/src/polite-lib/utils/dynamic_import.py
