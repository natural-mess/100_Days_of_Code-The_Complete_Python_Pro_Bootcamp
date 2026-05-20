from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B01NBKTPTS?th=1")
driver.get("https://www.python.org/")

# price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_euro.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link)

# Closes Chrome
driver.quit()

# # Deprecated - no longer needed
# chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"

# # keeps chrome open
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# # driver = webdriver.Chrome(executable_path=chrome_driver_path)
# # driver = webdriver.Chrome()
# driver = webdriver.Chrome(options=chrome_options)

# def test_eight_components():
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#     title = driver.title
#     assert title == "Web form"
#     driver.implicitly_wait(0.5)
#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#     text_box.send_keys("Selenium")
#     submit_button.click()
#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"

#     # Closes Chrome
#     # driver.quit()
#     # Close tab
#     driver.close()


# test_eight_components()
