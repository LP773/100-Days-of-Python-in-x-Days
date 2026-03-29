import datetime as dt
import smtplib
import random
import pandas as pd
import os

now = dt.datetime.now()
day = now.day
month = now.month

# My solution may be overly complicated
with open("birthdays.csv", "r") as birthdays_file:
     birthdays = pd.read_csv(birthdays_file)
     birthday_dict = birthdays.to_dict(orient="records")

     for item in range(len(birthday_dict)):
         if month == birthday_dict[item]['month'] and day == birthday_dict[item]['day']:
            letter_templates = "./letter_templates"
            letters = [f for f in os.listdir(letter_templates)]
            random_letter = random.choice(letters)
            with open(f"./letter_templates/{random_letter}", "r") as letter:
                letter_content = letter.read()
            modified_letter = letter_content.replace("[NAME]", f"{birthday_dict[item]['name']}")
            my_email = "email"
            password = "password"
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(my_email, password)
                smtp.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=f"Subject:Happy Birthday\n\n{modified_letter}")
            smtp.close()
