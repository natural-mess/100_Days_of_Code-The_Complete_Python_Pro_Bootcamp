from selenium.common.exceptions import (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException,)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
driver.get("https://ozh.github.io/cookieclicker/")

# Select language
## Wait for the language selection window appear, time out in 10s
lang_select_en = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
## Move to the center of an element with pressing and releasing the left mouse button
ActionChains(driver).click(lang_select_en).perform()

# Spamming cookie button
## Here, after selecting language, Cookie Clicker rebuilds parts of the page with JavaScript.
### During/after rebuild, the old bigCookie node is destroyed and a new one is created.
## Wait until the language selection element is replaced by the new page DOM
WebDriverWait(driver, 10).until(EC.staleness_of(lang_select_en))

# Timeout at 5 minutes
timeout = time.time() + 60*5
# Test tinout at 10s
# timeout = time.time() + 15

time_to_upgrade = time.time()
# Upgrade every x seconds
UPGRADE_EVERY = 5

ONE_MIN = 1*60
print_every_one_min = time.time()
count_min = 1

cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'bigCookie')))

while True:
    # Stop the bot after timeout
    if time.time() > timeout:
        break
    
    # Upgrade
    if time.time() - time_to_upgrade > UPGRADE_EVERY:
        products = driver.find_elements(By.CSS_SELECTOR, value='.product.unlocked.enabled')
        if products:
            products[-1].click()
        # Update time
        time_to_upgrade = time.time()

    # Click cookie
    try:
        cookie.click()
    except (StaleElementReferenceException, ElementClickInterceptedException):
        try:
            cookie = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "bigCookie"))
            )
            cookie.click()
        except TimeoutException:
            # UI is transiently rebuilding; skip this tick and continue loop
            pass

    # Print every 1min
    if time.time() - print_every_one_min > ONE_MIN:
        print(f"{count_min} minute(s) has passed")
        count_min += 1
        print_every_one_min = time.time()

print("Bot terminated, checking cookies per second...")
try:
    cps_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookiesPerSecond"))).text
    print("cookies/second :", cps_text.split()[-1] if cps_text else "N/A")
except (StaleElementReferenceException, TimeoutException):
    print("cookies/second : unavailable")

# Closes Chrome
driver.quit()