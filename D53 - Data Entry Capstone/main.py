from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

form_url = "https://forms.gle/6hdx7LDyow9jScX86"
zillow_clone = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(zillow_clone)
soup = BeautifulSoup(response.content, "html.parser")
price_list= []

price = soup.find_all("span", {"data-test": "property-card-price"})
for i in range(len(price) - 1):
    if "+" in price[i].text:
        price_list.append(price[i].text.split('+')[0])
    else:
        if "/" in price[i].text:
            price_list.append(price[i].text.split('/')[0])

address_list = []
address = soup.find_all("address", {"data-test": "property-card-addr"})
for i in range(len(address) - 1):
    address_list.append(address[i].text.split('\n')[1].strip())

links_list = []
links = soup.select(".StyledPropertyCardDataWrapper a")

for i in range(len(links) - 1):
    links_list.append(links[i].get('href'))

print(links_list)

driver = webdriver.Firefox()
driver.get(form_url)
wait = WebDriverWait(driver, 10)

for i in range(len(address_list) - 1):
    time.sleep(1)
    inputs = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")
    submit_btn = wait.until(presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Submit"]')))

    inputs[0].send_keys(address_list[i])
    inputs[1].send_keys(price_list[i])
    inputs[2].send_keys(links_list[i])
    submit_btn.click()
    time.sleep(1)
    anotha_one_btn = wait.until(presence_of_element_located((By.XPATH, '//a[text()="Submit another response"]')))
    anotha_one_btn.click()

driver.close()
driver.quit()

