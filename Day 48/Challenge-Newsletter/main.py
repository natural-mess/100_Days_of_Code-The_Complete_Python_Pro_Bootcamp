from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("My Firstname")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("My Lastname")

email = driver.find_element(By.NAME, value="email")
email.send_keys("myemail@email.com")

sign_up_btn = driver.find_element(By.CLASS_NAME, value='btn')
sign_up_btn.click()

# Closes Chrome
# driver.quit()