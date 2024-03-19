"""
    Polite Lib
    Utils
    Mathy

"""


def percentize(part: int, whole: int, round_to: int = 1, invert: bool = False) -> float:
    """Get the percent value that a part is from a whole.
    :unit-test: TestSharedUtilMisc::test__percentize
    """
    if part == 0 or whole == 0:
        return 0
    per = (part * 100) / whole
    per = round(per, round_to)
    if invert:
        per = percent_invert(per)
    return per


def percent_invert(percentage: float) -> float:
    """Get the inverse of a percentage."""
    diff = 100 - percentage
    return diff

# End File: polite-lib/src/polite_lib/utils/mathy.py
