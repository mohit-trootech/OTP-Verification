"""Custom Utility Classes"""


class MobileNumberMisMatch(Exception):
    """Mobile Number Mismatch Custom Error if Number length is not 10 and number is not numeric"""

    def __init__(self, message: str) -> None:
        """
        custom error class to throw mobile Number Mismatch Error
        @param message: str
        """
        self.message = message
