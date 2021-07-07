import requests
import os

LOGNAME = os.environ.get('LOGNAME')
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/61506f993bbc3e2625a5074516004c11/flightDeals/users"

print("Welcome to tomuchan's FLIGHT Club.")
print("We find the bet flight details and email you.")
FIRST_NAME = input("What is your first name?\n")
LAST_NAME = input("What is your last name?\n")
EMAIL = input("What is your email?\n")
TYPE_EMAIL = input("Type you email again.\n")


def send_data():
    sheet_input = {
        "user": {
            "firstName": FIRST_NAME,
            "lastName": LAST_NAME,
            "email": EMAIL
        }
    }

    auth = (LOGNAME, "P0kem0ns1ta1na")

    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=SHEETY_USERS_ENDPOINT,
        json=sheet_input,
        auth=auth, headers=headers)
    print(response)
    print(sheet_input)


if EMAIL == TYPE_EMAIL:
    send_data()
else:
    print("email is false")
