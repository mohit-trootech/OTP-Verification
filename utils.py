"""Custom Utility Classes"""
from datetime import datetime, timedelta


class MobileNumberMisMatch(Exception):
    """Mobile Number Mismatch Custom Error if Number length is not 10 and number is not numeric"""

    def __init__(self, message: str) -> None:
        """
        custom error class to throw mobile Number Mismatch Error
        @param message: str
        """
        self.message = message


def time_difference(time_obj: datetime) -> timedelta:
    """
    function to return the total seconds between two time object
    @param time_obj: datetime
    @return: timedelta
    """
    return (datetime.now().replace(microsecond=0) - time_obj).total_seconds()
