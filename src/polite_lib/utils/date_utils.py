"""
    Polite Lib
    Utils
    Date Utilities
    Testing
        Unit Test File: tests/unit/shared/utils/test_date_utils.py
        7/7

"""
from datetime import datetime
import logging

import arrow

from . import mathy


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
        logging.warning("Could not parse date string value %s with format: %s" % (
            the_str, parse_fmt))
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
    """Get the difference in seconds between to Arrow dates in seconds.
    :unit-test: TestDateUtils::test__time_diff
    """
    diff = end_time - start_time
    return diff.seconds


def time_diff_human(start_time: arrow.arrow.Arrow, end_time: arrow.arrow.Arrow) -> str:
    """Get the difference in seconds between to Arrow dates in a human readable format.
    @todo: Add more time cutts. Maybe create a decimal to base 60 for remainders.
    :unit-test: TestDateUtils::test__time_diff_human
    """
    diff_sec = time_diff(start_time, end_time)
    if diff_sec < 120:
        return f"{diff_sec} seconds"
    elif diff_sec < 3600 and diff_sec >= 5400:
        diff_mins = str(round(diff_sec / 60, 0))[:-2]
        return f"{diff_mins} minutes"
    # elif diff_sec > 5400:
    #     diff_hours = str(round(diff_sec / 3600, 2))
    #     print("here")
    #     return f"{diff_hours} hours"
    else:
        diff_mins = str(round(diff_sec / 60, 0))[:-2]
        return f"{diff_mins} minutes"


def elsapsed_time_human(timespent: float) -> str:
    """Get a human format of an elapse time value. Input will likely come from a TimeDelta objet,
    supplying just the seconds difference.
    :unit-test: TestDateUtils:
    """
    if timespent <= 120:
        if timespent == 1:
            unit = "second"
        else:
            unit = "seconds"
        rounded_value = round(timespent, 0)
        return f"{rounded_value} {unit}"
    if timespent >= 120 <= 5400:
        unit = "minutes"
        base = round(timespent / 60, 0)
        base = str(base)[:-2]
        seconds = timespent % 60
        if seconds != 0:
            if seconds < 10:
                seconds = ":0%s" % seconds
            else:
                seconds = ":%s" % seconds
        else:
            seconds = ""
        return '%s%s minutes' % (base, seconds)
    else:
        return '%s hours' % round(timespent / 3600, 2)

# def base100_to_base60(num):
#     """Converts an integer in base 100 system to a base 60 number.

#     Args:
#         num: The integer to convert.

#     Returns:
#         A string representing the base 60 equivalent of the input number.
#     """

#     if num == 0:
#         return "0"
#     digits = []
#     while num > 0:
#         digits.append(str(num % 60))
#         num //= 60
#     digits.reverse()
#     return ''.join(digits)


# def base_100_to_60(value: int) -> str:
#     """Convert a base 100 value to a base 60 value. This is helpful for taking a decimal and
#     returning a value which would represent seconds or minutes.
#     """
#     if value > 1:
#         raise ValueError("cannot convert value %s to a a base 60" % value)
#     value = value * 100
#     ret = round((100 * value) / 60, 2)
#     ret = str(ret)[:-2]
#     if len(ret) == 1:
#         ret = "0" + ret
#     return ret

# End File: polite-lib/src/polite-lib/utils/date_utils.py
