"""Handle Database using Class"""
import sqlite3
from sqlite3 import connect

import constant


class DatabaseOtp:
    """This class handles and manages a database to store and fetch OTPs. It offers an organized and reliable way to
    store and retrieve OTPs in a database, making it a valuable tool for applications that require secure
    authentication or password reset processes."""

    def __init__(self) -> None:
        """create instance variable for object"""
        self.db = connect(constant.DB)
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS otp (id INTEGER PRIMARY KEY, "
                            "number int, "
                            "sending_time varchar(32),"
                            "otp_number varchar(6),"
                            "status varchar(10));")

    def create_otp_entry(self, number: int, otp: str) -> None:
        """
        create an otp entry with the following details in database,
        (id: serial, number, datetime: current, otp, status: pending)
        @param number: int
        @param otp:
        """
        try:
            self.cursor.execute("INSERT INTO otp (number, sending_time, otp_number, status) VALUES"
                                f"({number}, '{str(constant.CURRENT_TIME)}', '{otp}', '{constant.STATUS_PENDING}');")
            self.db.commit()
        except sqlite3.OperationalError as e:
            print(constant.OPERATIONAL_ERROR, e)
        except Exception as e:
            print(constant.UNKNOWN_ERROR, e)

    def get_last_otp_data(self, number: int) -> tuple:
        """
        get last generated otp data
        @param number: int
        @return: tuple
        """
        try:
            data = self.cursor.execute(f"SELECT * FROM otp WHERE number = {number} and status = 'Pending' ORDER BY "
                                       f"sending_time DESC;")
            return data.fetchall()[0]
        except sqlite3.OperationalError as e:
            print(constant.OPERATIONAL_ERROR, e)
        except IndexError:
            print("No Otp Generated for Number {}".format(number))
        except Exception as e:
            print(constant.UNKNOWN_ERROR, e)

    def status_update(self, otp_data: tuple, status: str) -> None:
        """
        update status in database execution
        @param otp_data: int
        @param status: str
        """
        self.cursor.execute(f"UPDATE otp SET status = '{status}' where id = {otp_data[0]}")
        self.db.commit()


if __name__ == "__main__":
    obj = DatabaseOtp()
    x = obj.get_last_otp_data(constant.TEST_NUMBER)
    obj.status_update(x, constant.STATUS_SUCCESS)

