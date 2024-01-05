"""
    Polite Lib
    Utils
    Mathy

"""


def percentize(part: int, whole: int, round_int: int = 1) -> float:
    """Get the percent value that a part is from a whole.
    :unit-test: TestSharedUtilMisc:: test__percentize
    """
    if part == 0 or whole == 0:
        return 0
    per = (part * 100) / whole
    per = round(per, round_int)
    return per

# End File: polite-lib/src/polite_lib/utils/mathy.py
