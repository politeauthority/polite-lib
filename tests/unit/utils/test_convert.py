
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
        assert "0B" == convert.bytes_to_human(0)
        size = 4537715000
        result = convert.bytes_to_human(size)
        expected = "4.23 GB"
        assert expected == result

    def test__fahrenheit_to_celcius(self):
        """
        :method: xlate.fahrenheit_to_celcius
        """
        assert convert.fahrenheit_to_celcius(100) == 37.8

    def test__celcius_to_fahrenheit(self):
        """
        :method: xlate.celcius_to_fahrenheit
        """
        assert convert.celcius_to_fahrenheit(37.8) == 100

# End File: politeauthority/polite-lib/test/unit/utils/convert.py
