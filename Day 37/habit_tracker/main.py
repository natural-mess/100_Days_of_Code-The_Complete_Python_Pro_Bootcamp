import requests
from datetime import datetime

USERNAME = "rocky0405"
TOKEN = "awefawgfdgdrhjthjkrt435"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create account, only need to run it once
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
    "timezone": "Europe/Paris",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_date = datetime.today().strftime("%Y%m%d")

pixel_creation_param = {
    "date" : pixel_date,
    "quantity": "10",
}

# print(datetime.today().strftime("%Y%m%d"))
# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_param, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_date}"

pixel_update_param = {
    "quantity": "5.5",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_param, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_date}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)