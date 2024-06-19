
# OTP Validation Python

API, Database & Class Implementation Python Project to Validate OTP Real Time Send and Validation & Updates Database for the Same Status.

- Takes Number input from User and Validates the Number based on criteria ie. Number Must be 10 Digit & all integer values.
- then, OTP will generated using random module of python
- then, 'Vonage API' is used to send OTP, if OTP sends successfully return True else False.
- if True, then create a entry for OTP details in Database, and execute validate otp method.
- Validation of OTP is based on following Criteria ie. OTP must be entered within 60 seconds, OTP must be six digit integer value, OTP must be entered in 5 Tries.
- If Validation passed following criteria then Validate OTP and Update status for same as Success.
- Else Throw error Message for same, and update database entry for Failed.




## Documentation Reference

 - [Vonage Developer](https://www.vonage.com/developer-center/)
 - [GitHub README](https://github.com/mohit-trootech/Lyrics-Fetch-DB)

## Installation

_**Prerequisite: Install Python into Your System, Install Required Libraries ie. requests, sqlite3, Vonage**_

- Install my-project with git clone

```
  git clone https://github.com/mohit-trootech/Lyrics-Fetch-DB
  cd Lyrics-Fetch-DB
```
    
- Vonage Server SDK

```
pip install vonage


***This is the Python server SDK for Vonage's API. To use it you'll need a Vonage account. Sign up for free at vonage.com.***
```
-  Create New Files

```
  touch constants.py


**Read Documentation to Generate Api Key & Secret
  Create Reference Constants Variables for Error Free Execution**
```

- Run Python Files

```
  python otp.py
```
