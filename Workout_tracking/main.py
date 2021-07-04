import requests
import datetime as dt
import os

now = dt.datetime.today()
date = now.date()
DATETIME = date.strftime('%d/%m/%Y')
NOWTIME = now.strftime('%X')

NUTRITIONIX_API_ID = os.environ.get('NUTRITIONIX_API_ID')
NUTRITION_API_KEY = os.environ.get('NUTRITION_API_KEY')
SHEETY_BASIC = os.environ.get('SHEETY_BASIC')
LOGNAME = os.environ.get('USER')
PASSWORD = os.environ.get('SHEETY_PASS')

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEET_API = os.environ.get('SHEET_ENDPOINT')


headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITION_API_KEY,
    "Content-Type": "application/json"
}

# 適当な設定
params = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 80.0,
    "age": 28
}
response = requests.post(url=url, json=params, headers=headers).json()


for exercise in response["exercises"]:
    sheet_input = {
        "workout": {
            "date": DATETIME,
            "time": NOWTIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


sheet_post = {
    "email": {
        "name": "トムちゃん",
        "email": os.environ.get("GOOGLE_EMAIL"),
    }
}

basic = f"Basic {SHEETY_BASIC}"

auth = (LOGNAME, PASSWORD)


post_sheet = requests.post(
    url=SHEET_API, json=sheet_input, auth=auth)

print(post_sheet.text)
