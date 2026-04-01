import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
alpha_api_url = "https://www.alphavantage.co/query?"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "apikey": os.getenv("ALPHA_API_KEY"),
    "symbol": "TSLA",
    "COMPANY_NAME": "Tesla Inc"
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Ran out of requests... so to continue just saved and using data locally
#request = requests.get(alpha_api_url, params=stock_parameters)
#data = request.json()

with open("stock_data_file.json", "r") as stock_data_file:
    stock_data = json.load(stock_data_file)

previous_day = 0
day_before_previous = 1
data_dates = [item for item in stock_data["Time Series (Daily)"]]
datapoint_1 = float(stock_data["Time Series (Daily)"][data_dates[previous_day]]["4. close"])
datapoint_2 = float(stock_data["Time Series (Daily)"][data_dates[day_before_previous]]["4. close"])

change = datapoint_1-datapoint_2
percentage = round((change / float(datapoint_1)) * 100)
up_down = ""
if percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(percentage) > 5:
    news_api_url = "https://newsapi.org/v2/everything?"
    news_parameters = {
        "q": "Tesla",
        "apiKey": os.getenv("NEWS_API_KEY"),
    }

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    #request = requests.get(news_api_url, params=news_parameters)
    #news_data = request.json()

    with open("news_data_file.json", "r") as news_data_file:
        news_data = json.load(news_data_file)
        articles = news_data["articles"]

    # My way of getting the first 3 articles but then video mentioned slice
    # for item in range(0, 3):
    #     top_articles = articles[item]['title']
    #     print(top_articles)

    three_articles = articles[:3]

    # My way...
    # for article in three_articles:
    #     print(f"Headline: {article["title"]}")
    #     print(f"Brief: {article["description"]}")

    # Alternative way shown in video
    formatted_articles = [f"{stock_parameters["symbol"]}: {up_down}{percentage}%\nHeadline: {article["title"]} \nBrief: {article["description"]}\n" for article in three_articles]
    for article in formatted_articles:
        print(article)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

