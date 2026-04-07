from selenium import webdriver
import os
import  dotenv
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

dotenv.load_dotenv('.env')

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        username_field = self.wait.until(presence_of_element_located((By.NAME, "email")))
        password_field = self.wait.until(presence_of_element_located((By.NAME, "pass")))
        username_field.send_keys(os.environ['INSTAGRAM_USER'])
        time.sleep(1)
        password_field.send_keys(os.environ['INSTAGRAM_PASS'])
        time.sleep(1)
        log_in_button = self.wait.until(ec.element_to_be_clickable((By.XPATH,
                                                               "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/form/div/div[1]/div/div[3]/div/div")))
        time.sleep(1)
        log_in_button.click()

        # time.sleep(5)
        # code_submit = self.wait.until(ec.element_to_be_clickable((By.XPATH,
        #                                                      '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div')))
        # code_submit.click()

        save_no = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//div[contains(text(), "Not now")]')))
        save_no.click()
        time.sleep(1)
        notifications_no = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not Now")]')))
        notifications_no.click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/boilingpointgroup")
        follower_open = self.wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/section/main/div/div/header/div/section[2]/div[1]/div[3]/div[2]/a/span')))
        follower_open.click()

        # follower_window = self.driver.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_window)
        #     time.sleep(1)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='_aaco']")
        follow = 1
        for btn in follow_buttons:
            btn.click()
            time.sleep(1)
            follow += 1
            if follow == 5:
                break

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

