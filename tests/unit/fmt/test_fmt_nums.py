"""
    Polite Lib
    Test Format Numbers
    Tests File: polite-lib/src/polite-lib/utils/fmt_numbers.py

"""
from polite_lib.fmt import fmt_nums


class TestFmtNums:

    def test__add_commas(self):
        """Tests that we add commas in the correct places.
        :method: fmt_numbers.add_commas()
        """
        assert fmt_nums.add_commas(1000) == "1,000"
        assert fmt_nums.add_commas(10.52) == "10.52"

    def test__fmt_currency(self):
        """
        :method: fmt_numbers.fmt_currency()
        """
        assert fmt_nums.fmt_currency(1000) == "$1,000.00"
        assert fmt_nums.fmt_currency(.60) == "$0.60"
        assert fmt_nums.fmt_currency(5.6) == "$5.60"


# End File: cver/tests/unit/shared/utils/test_fmt_numbers.py
