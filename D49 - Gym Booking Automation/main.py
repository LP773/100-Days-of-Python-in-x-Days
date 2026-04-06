from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

ACCOUNT_EMAIL = "my_email@test.com"
ACCOUNT_PASSWORD = "password"
GYM_URL = "https://appbrewery.github.io/gym/"

# ----------------  Step 1 - Setup, Firefox Profile and Basic Navigation ----------------
profile_path = os.path.join(os.getcwd(), "firefox_profile")
profile = FirefoxProfile(profile_path)

options = Options()
options.add_argument("-profile")
options.add_argument(profile_path)
driver = webdriver.Firefox(options=options)
driver.get(url=GYM_URL)

# ----------------  Step 2 - Automated Login ----------------
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
login_button.click()

email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
password_input = driver.find_element(By.ID, "password-input")
submit_button = driver.find_element(By.ID, "submit-button")

email_input.send_keys(ACCOUNT_EMAIL)
password_input.send_keys(ACCOUNT_PASSWORD)
submit_button.click()
wait.until(presence_of_element_located((By.ID, "schedule-page")))

# ----------------  Step 3 - Book Class ----------------
booked_classes = 0
waitlisted_classes = 0
already_booked_classes = 0
total_booked_classes = 0

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text
    if "Tomorrow" in day_title:
        day_title = day_title.split("(")[1].replace(')', '')
    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name']").text
            class_btn = card.find_element(By.CSS_SELECTOR, "button[id^='book-button']")

# ----------------  Step 4 - Check Status ----------------
            if class_btn.text == "Booked":
                already_booked_classes += 1
                print(f"Already booked: {class_name} on {day_title}")
            elif class_btn.text == "Waitlisted":
                already_booked_classes += 1
                print(f"Already waitlisted: {class_name} on {day_title}")
            elif class_btn.text == "Join Waitlist":
                class_btn.click()
                waitlisted_classes += 1
                print(f"Joined waitlist for: {class_name} on {day_title}")
            elif class_btn.text == "Book Class":
                class_btn.click()
                booked_classes += 1
                print(f"Booked class for: {class_name} on {day_title}")
            total_booked_classes = booked_classes+waitlisted_classes+already_booked_classes

# print("\n--- BOOKING SUMMARY ---")
# print(f"Classes booked: {booked_classes}")
# print(f"Waitlists joined: {waitlisted_classes}")
# print(f"Already booked/waitlisted: {already_booked_classes}")
# print(f"Total Tuesday and Thursday 6pm classes processed: {booked_classes+waitlisted_classes+already_booked_classes}")

# ----------------  Step 5 - Verification ----------------
expected_classes = 0
my_bookings = driver.find_element(By.ID, "my-bookings-link")
my_bookings.click()
wait.until(presence_of_element_located((By.ID, "my-bookings-page")))

print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
booking_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-']")
for card in booking_cards:
    class_name = driver.find_element(By.CSS_SELECTOR, "h3[id^='booking-class-name-booking']").text
    print(f"✅ Verified: {class_name}")
    expected_classes += 1

waitlist_cards = card.find_elements(By.CSS_SELECTOR, "div[id^='waitlist-card-']")
for card in waitlist_cards:
    class_name = driver.find_element(By.CSS_SELECTOR, "h3[id^='waitlist-class-name-waitlist']").text
    print(f"✅ Verified: {class_name}")
    expected_classes += 1

if expected_classes != total_booked_classes:
    print(f"Expected {expected_classes} classes, but found {total_booked_classes} classes \nDifference: {expected_classes-total_booked_classes}")
else:
    print("\n--- VERIFICATION RESULT ---")
    print("Expected:", expected_classes)
    print("Found:", total_booked_classes)
    print("✅ SUCCESS: All bookings verified")

driver.close()
driver.quit()

