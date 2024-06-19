# import vonage
#
# client = vonage.Client(key="", secret="wR8CYRRbK7DfiEzL")
# sms = vonage.Sms(client)
#
# responseData = sms.send_message(
#     {
#         "from": "Mohit-Trootech",
#         "to": 917877287800,
#         "text": 4584,
#     }
# )
#
#
# if responseData["messages"][0]["status"] == "0":
#     print("Message sent successfully.")
# else:
#     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
import random
import math
x = ""
for i in range(6):
    x += str(math.floor(random.random() * 10))
print(x)
