from gettext import find

from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PROMISED_DOWN = 1000
PROMISED_UP = 1000

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

ACCOUNT_EMAIL = os.environ.get("Y_EMAIL") # The email you registered with
ACCOUNT_PASSWORD = os.environ.get("Y_PASSWORD")     # The password you used during registration
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
SPEED_TEST_URL = "https://www.speedtest.net"

class InternetSpeedTwitterBot:
    def __init__(self):
        # keeps chrome open
        self._chrome_options = webdriver.ChromeOptions()
        self._chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self._chrome_options)

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(f"{SPEED_TEST_URL}")
        start_btn = WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.CLASS_NAME, "js-start-test")))
        start_btn.click()

        WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located((By.CLASS_NAME, "download-speed")))
        down = self.driver.find_element(By.CLASS_NAME, "download-speed")
        WebDriverWait(self.driver, 180).until(lambda _: down.text != "—")
        self.down = down.text
        print(self.down)

        WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located((By.CLASS_NAME, "upload-speed")))
        up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        WebDriverWait(self.driver, 180).until(lambda _: up.text != "—")
        self.up = up.text
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get(f"{Y_LOGIN_URL}")
        # login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "y-login-link")))
        # login_btn.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "y-login-wrap")))
        email_input = self.driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys(ACCOUNT_EMAIL)
        pwd_input = self.driver.find_element(By.ID, "password")
        pwd_input.clear()
        pwd_input.send_keys(ACCOUNT_PASSWORD)

        submit_btn = self.driver.find_element(By.CLASS_NAME, "y-login-submit")
        submit_btn.click()

        tweet = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "tweet-compose")))
        # tweet = self.driver.find_element(By.ID, "tweet-compose")
        tweet.clear()
        tweet.send_keys(f"Hey Internet Provider, "
                              f"why is my internet speed "
                              f"{self.down}down/{self.up}up "
                              f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up")
        post_btn = self.driver.find_element(By.CLASS_NAME, "y-btn-accent")
        post_btn.click()

if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()