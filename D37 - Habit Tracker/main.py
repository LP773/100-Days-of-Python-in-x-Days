import requests
import os
from dotenv import load_dotenv
import datetime

USERNAME = "lp8"

load_dotenv()

pixela_user_api = "https://pixe.la/v1/users"
user_parameters = {
    "token": os.getenv("TOKEN"),
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_config = {
    "id": "graph1",
    "name": "Eating Graph",
    "unit": "Times",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": os.getenv("TOKEN"),
}


def create_user():
    response = requests.post(pixela_user_api, json=user_parameters)
    print(response.text)

def create_graph():
    pixela_graph_api = f"{pixela_user_api}/{USERNAME}/graphs"

    response = requests.post(pixela_graph_api, json=graph_config, headers=headers)
    print(response.text)

def add_pixel():
    date = input("What date are you trying to add? (Format: YYYYmmDD): ")
    amount = input("How many times did you eat today?: ")
    pixela_add_api = f"{pixela_user_api}/{USERNAME}/graphs/{graph_config['id']}"
    body = {
        "date": date,
        "quantity": amount,
    }

    response = requests.post(pixela_add_api, json=body, headers=headers)
    print(response.text)

def update_pixel():
    date = input("What date are you trying to update? (Format: YYYYmmDD): ")
    amount = input(f"How many times did you ACTUALLY eat on {date}?: ")
    pixela_update_api = f"{pixela_user_api}/{USERNAME}/graphs/{graph_config['id']}/{date}"
    body = {
        "quantity": amount,
    }

    response = requests.put(pixela_update_api, json=body, headers=headers)
    print(response.text)

def delete_pixel():
    date = input("What date are you embarrassed about? (Format: YYYYmmDD): ")
    pixela_delete_api = f"{pixela_user_api}/{USERNAME}/graphs/{graph_config['id']}/{date}"

    response = requests.delete(pixela_delete_api, headers=headers)
    print(response.text)