
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
        :method: convert.bytes_to_human
        """
        assert "0B" == convert.bytes_to_human(0)
        size = 4537715000
        result = convert.bytes_to_human(size)
        expected = "4.23 GB"
        assert expected == result

    def test__fahrenheit_to_celcius(self):
        """
        :method: convert.fahrenheit_to_celcius
        """
        assert convert.fahrenheit_to_celcius(100) == 37.8

    def test__celcius_to_fahrenheit(self):
        """
        :method: convert.celcius_to_fahrenheit
        """
        assert convert.celcius_to_fahrenheit(37.8) == 100

    def test__miles_to_kilometers(self):
        """
        :method: convert.miles_to_kilometers
        """
        assert convert.miles_to_kilometers(1) == 1.6

    def test__kilometers_to_miles(self):
        """
        :method: convert.kilometers_to_miles
        """
        assert convert.kilometers_to_miles(1.6) == 1.0


# End File: politeauthority/polite-lib/test/unit/utils/convert.py
