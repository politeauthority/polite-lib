"""
    Polite Lib - Tests
    Hash Utils

"""
import pytest

from polite_lib.utils import hash as hashies


class TestHash:

    def test__md5_file(self):
        """Test that we convert a file's contents to a hash.
        :method: hash.md5_file()
        """
        with pytest.raises(FileNotFoundError):
            assert hashies.md5_file("/does-not-exist")

# End File: polite-lib/test/unit/utils/test_hash.py
