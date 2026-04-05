import requests
import json
import os

parameters = {
    "appid": "",
    "lat": 36.169941,
    "long": -115.139832,
    "cnt": 4,
}
api_calls = {
    "current_weather": f"https://api.openweathermap.org/data/2.5/weather?",
    "five_day": f"https://api.openweathermap.org/data/2.5/forecast?"
}

api_name = "five_day"
api_data_file = f"api_data_{api_name}.json"

if os.path.exists(api_data_file):
    with open(api_data_file, "r") as f:
        data = json.load(f)
else:
    response = requests.get(api_calls[api_name], params=parameters)
    print(api_calls[api_name])
    print(response.status_code)
    with open(api_data_file, 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4)

data_length = len(data['list']) - 1
weather_info = data['list']
weather_id_list = []
umbrella_or_not = False
for i in range(4):
    weather_id_list.append(weather_info[i]['weather'][0]['id'])
    if weather_id_list[i] < 700:
        umbrella_or_not = True
if umbrella_or_not:
    print("Umbrella yourself.")