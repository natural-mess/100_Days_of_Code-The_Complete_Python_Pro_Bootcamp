from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
import time

FACEBARK_EMAIL = "test@test.com"
FACEBARK_PASSWORD = "test_password"
TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/81IZKEYVqj9LQk4CKzN59iHHKLMBTdNH"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
driver.get(f"{TINDOG_URL}")


def safe_click(locator, timeout=10, retries=3):
    # Generic click helper with retries for stale/slow-loading elements
    for i in range(retries):
        try:
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
            return
        except (StaleElementReferenceException, TimeoutException):
            if i == retries - 1:
                raise
            time.sleep(0.5)

def login():
    # Find login button
    login_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-tindog-login")))
    login_btn.click()

    # Wait for login options
    # btn-facebark is there but is hidden, so using presence_of_element_located will not work
    facebark_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-facebark")))
    facebark_btn.click()

def facebark_login():
    # Locate the new opening window and switch to it
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    # print(driver.title)

    email = driver.find_element(By.ID, "email")
    email.send_keys(FACEBARK_EMAIL)

    pwd = driver.find_element(By.ID, "pass")
    pwd.send_keys(FACEBARK_PASSWORD)

    # fb_login_btn = driver.find_element(By.TAG_NAME, "button")
    # fb_login_btn.click()
    pwd.send_keys(Keys.ENTER)

    # Switch back to main window
    driver.switch_to.window(base_window)

def dismiss_requests():
    # These dialogs frequently re-render; always re-locate just before each click.
    safe_click((By.XPATH, "/html/body/main/div/div/form/button"))
    safe_click((By.XPATH, "/html/body/main/div/div/form/button[2]"))
    safe_click((By.XPATH, "/html/body/main/div/div/form/button"))

# def check_element(class_name):
#     try:
#         driver.find_element(By.CLASS_NAME, f"{class_name}")
#         return True
#     except NoSuchElementException:
#         return False

def close_match_popup_if_present():
    popups = driver.find_elements(By.CLASS_NAME, "match-popup")
    if not popups:
        return

    # If popup exists but is hidden, still nothing blocking clicks right now.
    if not popups[0].is_displayed():
        return

    safe_click((By.CSS_SELECTOR, ".match-popup a"))
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "match-popup")))
    return

def hit_like():
    for _ in range(20):
        # Always clear match popup first because it can block the like button.
        close_match_popup_if_present()

        try:
            safe_click((By.CLASS_NAME, "btn-like"), retries=5)
        except (ElementClickInterceptedException, TimeoutException):
            # TimeoutException is handled twice to create 2 layers, if safe_click failes to retry, program handles popup
            # Popup may have appeared between wait and click; close and continue loop.
            close_match_popup_if_present()
            continue

login()
facebark_login()
dismiss_requests()
hit_like()
driver.quit()
