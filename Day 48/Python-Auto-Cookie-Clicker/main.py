from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

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

while True:
    try:
        cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'bigCookie')))
        cookie.click()
    except StaleElementReferenceException:
        continue

# Closes Chrome
# driver.quit()