from bs4 import BeautifulSoup
import requests
import os
import dotenv

dotenv.load_dotenv()

# TELEGRAM
# https://api.telegram.org/bot<token>/METHOD_NAME
API_ENDPOINT = "https://api.telegram.org/bot"
TOKEN = os.environ['TELEGRAM_TOKEN']

# AMAZON
item_url = "https://www.amazon.com/dp/B0D8694QGZ?ie=UTF8&th=1"
headers = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:149.0) Gecko/20100101 Firefox/149.0"
}

# Scrape
threshold = 30
request = requests.get(item_url, headers=headers)
soup = BeautifulSoup(request.content, 'html.parser')
product = soup.find(name="span", id="productTitle").get_text().strip()
whole = soup.find(name="span", class_="a-price-whole")
fraction = soup.find(name="span", class_="a-price-fraction")
price = float(whole.text + fraction.text)

# Send Telegram message
if price < threshold:
    message = (f"""
The item you're watching 
<a href="{item_url}">{product}</a> 
has fallen <b><i>BELOW</i></b> the price threshold of <i>{threshold}</i>.

It is currently <b>{price}</b>.
""")
    parameters = {
        "chat_id": os.environ["TELEGRAM_CHAT_ID"],
        "text": message,
        "parse_mode": "HTML"
    }
    telegram_send = requests.post(f"{API_ENDPOINT}{TOKEN}/sendMessage", params=parameters)
    print(telegram_send.status_code, telegram_send.text)

