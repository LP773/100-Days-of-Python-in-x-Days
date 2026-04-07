from selenium import webdriver
import os
import  dotenv
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

dotenv.load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
BSKY_EMAIL = os.environ.get("BSKY_EMAIL")
BSKY_PASSWORD = os.environ.get("BSKY_PASSWORD")

class InternetSpeedBskyBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")
        go_button = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "div.start-button")))
        go_button.click()

        time.sleep(50)

        self.up = self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text
        self.down = self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text
        print(self.up, self.down)

    def make_post(self):
        self.driver.get("https://bsky.app")
        sign_in_button = self.wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/button")))
        sign_in_button.click()

        username_input = self.wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/input")))
        password_input = self.wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/input")))
        username_input.send_keys(os.environ["BSKY_EMAIL"])
        password_input.send_keys(os.environ["BSKY_PASSWORD"])
        time.sleep(1)
        submit_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/button[2]/div")))
        submit_button.click()

        post_button = self.wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/main/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/button")))
        post_button.click()
        time.sleep(1)
        post_contents = self.wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div")))
        post_contents.send_keys(f"Cox Fiber Internet (Wi-Fi). Eh. Could be higher. DL:{self.down}, UP:{self.up}")
        send_it_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/button[3]")
        time.sleep(1)
        send_it_button.click()

bot = InternetSpeedBskyBot()
bot.get_internet_speed()
bot.make_post()

