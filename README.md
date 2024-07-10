
# OTP Validation Python

This Python project will verify, dispatch, and update the status of one-time passwords (OTPs) in real time. 
- Initially, the user submits a mobile number, and the project verifies that the number is 10 digits in length and comprises only integer values.
- An OTP is then generated using Python's random module, and the Vonage API is employed to transmit the OTP. 
- Upon successful transmission of the OTP, an entry is created in the database to record the OTP details, and the OTP validation procedure is commenced. 
- Validation of the OTP is contingent upon the fulfillment of several conditions: the OTP must be entered within 60 seconds, must consist of six integer digits, and must be attempted no more than five times. 
- If the OTP satisfies all of these criteria, it is deemed valid, and its status is updated to "Success." 
-Otherwise, an error message is displayed, and the database entry is modified to "Failed."



## Documentation Reference

 - [Vonage Developer](https://www.vonage.com/developer-center/)
 - [GitHub README](https://github.com/mohit-trootech/OTP-Verification)

## Installation

_**Prerequisite: Install Python into Your System, Install Required Libraries ie. requests, sqlite3, Vonage**_

- Install my-project with git clone

```
  git clone https://github.com/mohit-trootech/OTP-Verification
  cd OTP-Verification
```
    
- Vonage Server SDK

```
pip install vonage


***This is the Python server SDK for Vonage's API. To use it you'll need a Vonage account. Sign up for free at vonage.com.***
```
-  Create New Files

```
  touch .env

[//]: # ( _Read Documentation to Generate Api Key & Secret Create Reference Constants Variables for Error Free Execution_ )
```

- Run Python Files

```
  python otp.py
```
