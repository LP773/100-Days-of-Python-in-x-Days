import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()
exercise = input("Tell me which exercise you did: ")

body = {
    "query": exercise
}
header = {
    "x-app-id": os.getenv("x-app-id"),
    "x-app-key":  os.getenv("x-app-key")
}
url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

request = requests.post(url, json=body, headers=header)

processed_exercise = request.json()["exercises"][0]["name"]
processed_duration = request.json()["exercises"][0]["duration_min"]
processed_calories = request.json()["exercises"][0]["nf_calories"]
print(request.status_code)

sheety_post_url = "https://api.sheety.co/e91c3d804dda3d2481e515b645ae4d84/myWorkouts/workouts"
date = datetime.now()
formatted_date = date.strftime("%d/%m/%Y")
time = date.time().strftime("%H:%M:%S")

sheety_body = {
    "workout": {
        "date": formatted_date,
        "time": time,
        "exercise": processed_exercise,
        "duration": processed_duration,
        "calories": processed_calories
    }
}
sheety_header = {
    "Authorization": f"Bearer {os.getenv('authorization')}",
}

sheety_response = requests.post(sheety_post_url, json=sheety_body, headers=sheety_header)
print(sheety_response.status_code)

