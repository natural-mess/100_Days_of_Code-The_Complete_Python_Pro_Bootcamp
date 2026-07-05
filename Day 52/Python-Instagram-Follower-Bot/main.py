from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import (
    ElementClickInterceptedException,
)
from dotenv import load_dotenv
import os

load_dotenv("D:/API/EnvironmentVariables/.env")

SIMILAR_ACCOUNT = "chefsteps"   # the account whose followers you'll follow
USERNAME = os.environ.get("SHARE-A-NAAN_USERNAME")       # your Share-a-Naan (or Instagram) username (your email)
PASSWORD = os.environ.get("SHARE-A-NAAN_PASSWORD")
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

class InstaFollower:
    def __init__(self):
        # keeps chrome open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(f"{LOGIN_URL}")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "naan-login-panel")))

        username_input = self.driver.find_element(By.ID, "username")
        username_input.clear()
        username_input.send_keys(USERNAME)

        pwd_input = self.driver.find_element(By.ID, "password")
        pwd_input.clear()
        pwd_input.send_keys(PASSWORD)

        submit_btn = self.driver.find_element(By.CLASS_NAME, "naan-btn-primary")
        submit_btn.click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "popup-save-login")))
        save_info_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#popup-save-login .naan-popup-dismiss")))
        save_info_btn.click()
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "popup-notifications")))
        noti_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#popup-notifications .naan-popup-dismiss")))
        noti_btn.click()

    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "naan-profile-header")))

        follower_btn = self.driver.find_element(By.CLASS_NAME, "naan-followers-link")
        follower_btn.click()

        follower_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "followers-scroll")))
        for _ in range(5):
            # Setting scrollTop to scrollHeight means scroll to bottom
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_list)
            time.sleep(1)

    def follow(self):
        follow_list = self.driver.find_elements(By.CSS_SELECTOR, ".naan-follower-row .naan-follow-btn")
        for btn in follow_list:
            try:
                btn.click()
                WebDriverWait(self.driver, 10).until(lambda _: btn.text != "Follow")
            except ElementClickInterceptedException:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "naan-unfollow-card")))
                cancel_btn = self.driver.find_element(By.CLASS_NAME, "naan-unfollow-cancel")
                cancel_btn.click()
                time.sleep(1)


if __name__ == '__main__':
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()
