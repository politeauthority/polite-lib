"""
    Polite Lib
    Hash
    Tools for handling hashes

"""

import hashlib
import os


def md5_file(file_path: str) -> str:
    """Create an anchor link in html with a given anchor and title string to use."""
    if not os.path.exists(file_path):
        raise Exception("Path does not exist: %s" % file_path)
    open_file = open(file_path, 'rb').read()
    return hashlib.md5(open_file).hexdigest()


# End File: polite-lib/src/polite-lib/utils/hash.py
