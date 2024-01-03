"""
    Polite Lib
    Utils
    Date Utilities
    Testing
        Unit Test File: tests/unit/shared/utils/test_date_utils.py
        7/7

"""
from datetime import datetime

import arrow


def now() -> datetime:
    """Short hand to get now as UTC.
    :unit-test: TestSharedUtilsDateUtils.test__now
    """
    return arrow.utcnow().datetime


def json_date(the_datetime: datetime) -> str:
    """Get a JSON returnable value from a datetime.
    :unit-test: TestSharedUtilsDateUtils.test__json_date
    """
    if not the_datetime:
        return None
    return arrow.get(the_datetime).format('YYYY-MM-DD HH:mm:ss ZZ')


def json_date_out(the_datetime: datetime) -> str:
    """Get a JSON postable value from a datetime.
    :unit-test: TestSharedUtilsDateUtils.test__json_date_out
    """
    if not the_datetime:
        return None
    return arrow.get(the_datetime).format('YYYY-MM-DD HH:mm:ss ZZ')[:-7]


def json_date_now() -> str:
    """Get a JSON returnable value from now in UTC. Use this method for sending dates to the
    Cver Api
    :unit-test: TestSharedUtilsDateUtils.test__json_date_now
    """
    return arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ')[:-7]


def human_date(the_datetime: str) -> str:
    """Get a human date from a Datetime object, such as "2 hours ago". Input can be a string,
    datetime or arrow object.
    :unit-test: TestSharedUtilsDateUtils.test__human_date
    """
    if not the_datetime:
        return None
    if isinstance(the_datetime, str) and "+00:00" in the_datetime:
        the_datetime = the_datetime.replace("+00:00", "")
        the_datetime = the_datetime.strip()
    return arrow.get(the_datetime).humanize()


def get_as_utc(a_datetime: datetime):
    """Convert a datetime into a UTC Arrow object.
    :unit-test: TestSharedUtilsDateUtils.test__get_as_utc
    """
    a_utc_time = arrow.get(a_datetime)
    return a_utc_time.to('UTC')


def date_from_json(the_datetime: str, parse_fmt: str = None) -> arrow.arrow.Arrow:
    """Convert a string into a python native arrow object.
    :unit-test: TestSharedUtilsDateUtils.test__date_from_json
    """
    if not the_datetime:
        return None
    if not parse_fmt:
        parse_fmt = "YYYY-MM-DD HH:mm:ss ZZ"
    try:
        ret_datetime = arrow.get(the_datetime, parse_fmt)
    except arrow.parser.ParserError:
        ret_datetime = None
    return ret_datetime


def from_str(the_str: str, parse_fmt: str = None) -> arrow.arrow.Arrow:
    """Convert a string into a python native arrow object.
    :param the_str: Currently this is expected to look like "2023-11-02 18:16:45 +00:00"
    :unit-test: TestSharedUtilsDateUtils.test__date_from_json
    """
    if not the_str:
        return None
    if not parse_fmt:
        parse_fmt = "YYYY-MM-DD HH:mm:ss ZZ"
    try:
        ret_datetime = arrow.get(the_str, parse_fmt)
    except arrow.parser.ParserError:
        ret_datetime = None
    return ret_datetime


def interval_ready(last: datetime, interval_hours: int) -> bool:
    """Determine in a given datetime is older than the interval_hours. If we dont have a value for
    the last time, we'll assume the interval is ready.
    :unit-test: TestSharedUtilsDateUtils.test__interval_ready
    """
    if not last:
        return True
    now = arrow.utcnow()
    last = arrow.get(last)
    interval_seconds = 3600 * interval_hours
    diff = (now - last).total_seconds()
    if diff > interval_seconds:
        return True
    else:
        return False


def from_epoch(epoch_time: int) -> arrow.arrow.Arrow:
    """Get an Arrow date from an epoch time.
    :unit-test:
    """
    return arrow.get(datetime.fromtimestamp(epoch_time))


def time_diff(start_time: arrow.arrow.Arrow, end_time: arrow.arrow.Arrow) -> int:
    """Get the difference in seconds between to Arrow dates in seconds."""
    diff = end_time - start_time
    return diff.seconds


def time_diff_human(start_time: arrow.arrow.Arrow, end_time: arrow.arrow.Arrow) -> str:
    """Get the difference in seconds between to Arrow dates in a human readable format.
    @todo: Add more time cutts. Maybe create a decimal to base 60 for remainders.
    """
    diff_sec = time_diff(start_time, end_time)
    if diff_sec < 120:
        return f"{diff_sec} seconds"
    elif diff_sec < 3600:
        diff_mins = str(round(diff_sec / 60, 0))[-2]
        return f"{diff_mins} minutes"
    else:
        diff_mins = str(round(diff_sec / 60, 0))[-2]
        return f"{diff_mins} minutes"

# End File: polite-lib/src/polite-lib/utils/date_utils.py
