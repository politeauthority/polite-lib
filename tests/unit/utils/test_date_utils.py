"""
    Polite Lib
    Test Date Utils
    Tests File: polite-lib/src/polite-lib/utils/date_utils.py

"""
from datetime import datetime

import arrow

from polite_lib.utils import date_utils


class TestDateUtils:

    def test__now(self):
        """
        :method: date_util.now()
        """
        assert isinstance(date_utils.now(), datetime)

    def test__json_date(self):
        """
        :method: date_util.json_date()
        """
        assert isinstance(date_utils.json_date(arrow.utcnow().datetime), str)
        assert 26 == len(date_utils.json_date(arrow.utcnow().datetime))

    def test__json_date_now(self):
        """
        :method: date_util.json_date_now()
        """
        assert isinstance(date_utils.json_date_now(), str)
        assert 19 == len(date_utils.json_date_now())
        assert arrow.get(date_utils.json_date_now())

    def test__human_date(self):
        """
        :method: date_util.human_date()
        """
        now = arrow.utcnow()
        assert "just now" == date_utils.human_date(now)
        assert "2 hours ago" == date_utils.human_date(now.shift(hours=-2))

    def test__get_as_utc(self):
        """
        :method: date_util.get_as_utc()
        """
        assert isinstance(date_utils.get_as_utc(datetime.now()), arrow.arrow.Arrow)

    def test__date_from_json(self):
        """
        :method: date_util.date_from_json()
        """
        date_str = "2023-09-29 21:30:45 +00:00"
        assert isinstance(date_utils.date_from_json(date_str), arrow.arrow.Arrow)

    def test__from_str(self):
        """
        :method: date_utils.from_str()
        """
        assert not date_utils.from_str(None)
        assert not date_utils.from_str('2024-041-01 12:00:00')

    def test__interval_ready(self):
        """Test that we get the correct bool value from a datetime that is passed the interval
        setting.
        :method: date_util.interval_ready()
        """
        five_hours_ago = arrow.utcnow()
        five_hours_ago = five_hours_ago.shift(hours=-5)
        assert date_utils.interval_ready(five_hours_ago.datetime, 2)
        assert not date_utils.interval_ready(five_hours_ago.datetime, 10)

    def test__from_epoch(self):
        """Test that we can get an Arrow object from an epoch time.
        :method: date_util.from_epoch()
        """
        assert isinstance(date_utils.from_epoch(1703347823), arrow.arrow.Arrow)

    def test__time_diff(self):
        """Test that we can get an Arrow object from an epoch time.
        :method: date_util.time_diff()
        """
        start = arrow.get("2024-01-03T15:53:49Z")
        end = arrow.get("2024-01-03T15:55:04Z")
        assert 75 == date_utils.time_diff(start, end)

    def test__time_diff_human(self):
        """Test that we can get an Arrow object from an epoch time.
        :method: date_util.time_diff_human()
        """
        start = arrow.get("2024-01-03T15:53:49Z")
        end_1 = arrow.get("2024-01-03T15:55:04Z")
        end_2 = arrow.get("2024-01-03T16:55:04Z")
        end_3 = arrow.get("2024-01-03T18:04:04Z")
        assert "75 seconds" == date_utils.time_diff_human(start, end_1)
        assert "61 minutes" == date_utils.time_diff_human(start, end_2)
        assert "130 minutes" == date_utils.time_diff_human(start, end_3)

    def test__elsapsed_time_human(self) -> bool:
        """
        :method: date_util.elsapsed_time_human()
        """
        assert "1 second" == date_utils.elsapsed_time_human(1)
        assert "52 seconds" == date_utils.elsapsed_time_human(52)
        assert "61 seconds" == date_utils.elsapsed_time_human(61)
        assert "61 seconds" == date_utils.elsapsed_time_human(61)
        assert "2:05 minutes" == date_utils.elsapsed_time_human(125)
        assert "90 minutes" == date_utils.elsapsed_time_human(5400)

# End File: cver/tests/unit/shared/utils/test_date_utils.py
