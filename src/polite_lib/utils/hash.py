"""
    Polite Lib
    Hash
    Tools for handling hashes

"""

import hashlib
import os


def md5_file(file_path: str) -> str:
    """Get the MD5 hash of a given file's contents.
    :unit-test: TestHash::test__md5_file()
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("Path does not exist: %s" % file_path)
    open_file = open(file_path, 'rb').read()
    return hashlib.md5(open_file).hexdigest()


# End File: polite-lib/src/polite-lib/utils/hash.py
