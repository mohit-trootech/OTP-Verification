"""Python Project to Generate and Validate OTPs"""
import math
import random
from datetime import datetime
import vonage
import constant
from otp_database import DatabaseOtp


class MobileNumberMisMatch(Exception):
    """Mobile Number Mismatch Custom Error if Number length is not 10 and number is not numeric"""

    def __init__(self, message: str) -> None:
        """
        custom error class to throw mobile Number Mismatch Error
        @param message: str
        """
        self.message = message


class OTP(DatabaseOtp):
    """class to implement OTP generation and validation, along with a description of its functionality."""

    def __init__(self) -> None:
        """
        create Instances for otp Object
        """
        super().__init__()
        self.otp = ""

    def generate_otp(self) -> str:
        """
        otp generate using random method
        @return: str
        """
        for i in range(6):
            self.otp += str(math.floor(random.random() * 10))
        return self.otp

    def validate_otp(self, number: int) -> None:
        """
        method to validate otp checks time difference not more than 60 seconds &
        tries to match otp for 5 times else return failed
        @param number: int
        """
        otp_data = self.get_last_otp_data(number)
        time_difference = constant.CURRENT_TIME - datetime.strptime(otp_data[2],
                                                                    "%Y-%m-%d %H:%M:%S")
        tries = 5
        while True:
            try:
                if time_difference.total_seconds() > 60:
                    raise Exception(constant.EXPIRY_OTP)
                received_otp = int(input("Enter Received OTP: "))
                if received_otp == int(otp_data[-2]):
                    print(constant.VALIDATE_OTP)
                    self.status_update(otp_data, constant.STATUS_SUCCESS)
                    break
                else:
                    tries -= 1
                    if tries == 0:
                        print(constant.NO_TRY)
                        self.status_update(otp_data, constant.STATUS_FAILED)
                        break
                    else:
                        print(f"You are Left With {tries} Tries Try Again")
            except ValueError:
                tries -= 1
                print("Try Entering a Numeric OTP Received")
                self.status_update(otp_data, constant.STATUS_FAILED)
            except Exception as e:
                print(e)


class OtpSend(OTP):
    """This code implements a class that generates and send one-time passwords (OTPs)."""

    def __init__(self, number: int) -> None:
        super().__init__()
        self.receiver_number = number
        try:
            self.validate_number(self.receiver_number)
            otp = self.generate_otp()
            self.create_otp_entry(self.receiver_number, otp)
            if self.send_otp(self.receiver_number, otp):
                self.validate_otp(self.receiver_number)
        except Exception as e:
            print(constant.UNKNOWN_ERROR, e)

    @staticmethod
    def validate_number(number: int) -> None:
        """
        validate mobile number if length is 10 digit or not
        @param number: int
        """
        if len(str(number)) != 10:
            raise MobileNumberMisMatch(constant.NUMBER_ERROR)

    @staticmethod
    def send_otp(number: int, otp: str) -> bool:
        """
        vonage to Send API to Receiver Mobile Number
        @param number: int
        @param otp: str
        @return: bool
        """
        client = vonage.Client(key=constant.API_KEY_SMS, secret=constant.API_SECRET)
        sms = vonage.Sms(client)
        response_data = sms.send_message(
            {
                "from": "Mohit-Trootech",
                "to": f"91{number}",
                "text": otp,
            }
        )
        if response_data["messages"][0]["status"] == "0":
            print("Message sent successfully.")
            return True
        else:
            print(f"Message failed with error: {response_data['messages'][0]['error-text']}")
            return False


try:
    num = int(input("Enter Receiver's Phone Number\n:- Must be Numeric and 10 Digits: "))
    obj = OtpSend(num)
except ValueError as e:
    print(constant.NUMBER_ERROR, e)
except Exception as e:
    print(constant.UNKNOWN_ERROR, e)