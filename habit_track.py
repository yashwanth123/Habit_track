import requests
from datetime import datetime
USERNAME = username
TOKEN = code
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

Graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "learning calculator",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url = Graph_endpoint, json = graph_params, headers = headers)
# print(response.text)


Posting_init = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now()
posting_params = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many hours enter"),
}


response = requests.post(
    url=Posting_init, json=posting_params, headers=headers)
print(response.text)

update = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
new = {
    "quantity": 4.5,
}
#response = requests.post(url=update, json=new, headers=headers)
# print(response.text)

delete = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
#response = requests.post(url=delete, headers=headers)
# print(response.text)
