from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Connecting to Cookie Clicker
url = "https://ozh.github.io/cookieclicker/"
driver = webdriver.Firefox()
driver.get(url)

wait = WebDriverWait(driver, 10)
# Language Selection
english_lang = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
english_lang.click()

# Find GIANT COOKIE
giant_cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))

"""
Method buys Buildings
Technically buys the last item (or most expensive item) but if at time of check there is only 1 item in the list,
it will just buy that item.

I peeked a bit at the solution because I was stuck from overthinking how to implement this... I was thinking
comparing how many cookies we have versus the costs of the upgrades and dictionaries and all sorts of complicated things
"""
def buy_buildings():
    products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    if products:
        products[len(products) - 1].click()

"""
Method buys Upgrades
Works the same as buy_buildings
"""
def buy_upgrades():
    upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
    if upgrades:
        upgrades[len(upgrades) - 1].click()

timeout =  time.time() + 60 * 5 # 5 Minutes
next_check = time.time() + 5
while time.time() < timeout:
    giant_cookie.click()

    """
    Stats - realized I needed to initialize within the while loop or else it would stay its initial value (0)
    """
    # Amount of Cookies
    cookies = driver.find_element(By.ID, "cookies").text.strip().split("\n")[0] 
    #Split needs to be " " when cheat is a smaller number but when it passes xxx,xxx digits it becomes \n
    
    # Cookies per second
    cps = driver.find_element(By.ID, "cookies").text.strip().split(":")[1].strip()

    """
    I wanted to see if there was a way there could be multiple clicks (MORE CLICKS, MORE COOKIES)
    1. Suggestion was to use JavaScript but that seemed about the same if not slower than use .click()
    2. The second was to modify the game directly and that honestly... worked the best 🤪
    3. I later thought about changing how many cookies you get per click because even if you have a ton of cookies
    if it doesn't correlate with cps things do not unlock.
    
    So... of course I asked ChatGPT if I could inject a button to toggle or run this cheat. Or modify an existing one
    I couldn't get it to behave the way I wanted to :(.
    
    Comment out or remove lines 68-70 to stop cheats.
    """
    #Activate Cheat
    driver.execute_script("""
    Game.computedMouseCps = 10000;
    """)

    if time.time() >= next_check:
        buy_buildings()
        buy_upgrades()
        next_check += 1

    if time.time() >= timeout:
        print(f"You had {cookies} cookies and your cookies per second was {cps}")
        driver.quit()

