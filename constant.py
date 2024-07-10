"""Python Files to Store Constants"""
from datetime import datetime

STATUS_FAILED = "Failed"
STATUS_SUCCESS = "Success"
STATUS_PENDING = "Pending"
DB = "otp.db"

CURRENT_TIME = datetime.now().replace(microsecond=0)

# Errors
OPERATIONAL_ERROR = "Error in SQL Execution"
UNKNOWN_ERROR = "Unknown Exception Occurred"
EXPIRY_OTP = "Time Limit Reached Try Again with New OTP"
VALIDATE_OTP = "OTP Validation Successfully"
NO_TRY = "Try Again and Generate New OTP"
NUMBER_ERROR = "Mobile Number is Invalid, Must be 10 Digit and all Integer Numbers"
