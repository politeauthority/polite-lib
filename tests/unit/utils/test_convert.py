
"""
    Polite Lib
    Test
    Util - Concert
    Tests File: polite-lib/src/polite-lib/utils/convert.py

"""
from polite_lib.utils import convert


class TestUtilsConvert:

    def test__bytes_to_human(self):
        """
        :method: xlate.bytes_to_human
        """
        size = 4537715000
        result = convert.bytes_to_human(size)
        expected = "4.23 GB"
        assert expected == result


# End File: polite-lib/test/unit/utils/convert.py
