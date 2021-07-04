import requests
import datetime as dt
import os

now = dt.datetime.today()
date = now.date()

DATETIME = date.strftime('%Y%m%d')

USERNAME = os.environ.get('USER')
TOKEN = os.environ.get('TOKEN')
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers)
# print(response.text)

# post
post_pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

graph_params = {
    "date": DATETIME,
    "quantity": input("今日何キロ走った?"),
}

response = requests.post(
    url=post_pixela_endpoint,
    json=graph_params,
    headers=headers)
print(response.text)


# put
# put_pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATETIME}"

# put_params = {
#     "quantity": "10",
# }

# response = requests.put(
#     url=put_pixela_endpoint,
#     json=put_params,
#     headers=headers)

# print(response.text)

# delete

# delete_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATETIME}"

# response = requests.delete(url=delete_end_point, headers=headers)

# print(response.text)
