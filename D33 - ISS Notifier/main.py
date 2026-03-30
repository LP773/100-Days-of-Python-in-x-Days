import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 36.002729 # Your latitude
MY_LONG = -115.207128 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def within_range():
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5 and sunrise:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def is_night():
    if time_now.hour >= sunset and time_now.hour <= sunrise:
        return True
    else:
        return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if within_range() and is_night():
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login("email", "password")
        smtp_server.sendmail(
            from_addr="email",
            to_addrs="email",
            msg="Subject:TIME FOR TACO BELL\n\nThe ISS is at a Taco Bell near you!"
        )

