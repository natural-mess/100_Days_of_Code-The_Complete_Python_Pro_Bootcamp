from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException, TimeoutException)
import os
import time
from dotenv import load_dotenv

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

ACCOUNT_EMAIL = os.environ.get("GYM_ACCOUNT_EMAIL") # The email you registered with
ACCOUNT_PASSWORD = os.environ.get("GYM_ACCOUNT_PASSWORD")     # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Give Selenium it's own user profile. Create a chrome profile and store in chrome_profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
# Tell your Chrome Driver to use the directory you specified to store a "profile".
# That way every time you quit Chrome and re-run your Selenium script, it keeps all the preferences and settings from your profile.
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
driver.get(f"{GYM_URL}")

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    # Login
    login_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    # Input email and password
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)
    pwd_input = driver.find_element(By.ID, "password-input")
    pwd_input.clear()
    pwd_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()

    # Wait for schedule page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "schedule-page")))

retry(login, description="login")

total_tue_thu = 0
# Find all available booking days
booking_days = driver.find_elements(By.CSS_SELECTOR, "div[id^='day-group-']")

classes_booked = 0
waitlists_joined = 0
already_booked_waitlisted = 0

booking_list = []

def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    WebDriverWait(driver, 10).until(lambda _: booking_button.text == "Booked" or booking_button.text == "Join Waitlist")

for day in booking_days:
    day_title = day.find_element(By.TAG_NAME, "h2")
    
    # Find tuesday and thursday
    if "Tue" in day_title.text or "Thu" in day_title.text:
        # Find class at 6:00 PM
        day_classes = day.find_elements(By.CSS_SELECTOR, "p[id^='class-time-']")
        for class_ in day_classes:
            if "6:00 PM" in class_.text:
                class_card = class_.find_element(By.XPATH, "ancestor::div[@class='ClassCard_cardHeader__D9pf3']")
                class_name = class_card.find_element(By.TAG_NAME, "h3").text
                booking_btn = class_card.find_element(By.TAG_NAME, "button")
                if booking_btn.text == "Booked":
                    already_booked_waitlisted+=1
                    print(f"✓ Already booked: {class_name} on {day_title.text}")
                    booking_list.append({
                        'type': "[Booked]",
                        'class_name': class_name,
                        'date': day_title.text,
                    })
                elif booking_btn.text == "Waitlisted":
                    already_booked_waitlisted+=1
                    print(f"✓ Already on waitlist: {class_name} on {day_title.text}")
                    booking_list.append({
                        'type': "[Waitlisted]",
                        'class_name': class_name,
                        'date': day_title.text,
                    })
                elif booking_btn.text == "Join Waitlist":
                    # pass retry(lambda: book_class(booking_btn))
                    # retry stores that lambda as func
                    # retry calls func() with no args
                    # lambda runs book_class(booking_btn)
                    retry(lambda: book_class(booking_btn), description="Join Waitlist")
                    waitlists_joined+=1
                    print(f"✓ Joined waitlist for: {class_name} on {day_title.text}")
                    booking_list.append({
                        'type': "[New Waitlist]",
                        'class_name': class_name,
                        'date': day_title.text,
                    })
                elif booking_btn.text == "Book Class":        
                    retry(lambda: book_class(booking_btn), description="Booking")
                    classes_booked+=1
                    print(f"✓ Successfully booked: {class_name} on {day_title.text}")
                    booking_list.append({
                        'type': "[New Booking]",
                        'class_name': class_name,
                        'date': day_title.text,
                    })
                time.sleep(0.5)
                break

# print("\n--- BOOKING SUMMARY ---")
# print(f"New bookings: {classes_booked}")
# print(f"New waitlist entries: {waitlists_joined}")
# print(f"Already booked/waitlisted: {already_booked_waitlisted}")
total_tue_thu = classes_booked + waitlists_joined + already_booked_waitlisted
print(f"Total Tuesday & Thursday 6pm classes: {total_tue_thu}")

# print("\n--- DETAILED CLASS LIST ---")
# for booking in booking_list:
#     print(f"\t• {booking['type']} {booking['class_name']} on {booking['date']}")

def get_my_bookings():
    verification_count = 0
    print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
    # Navigate to My Bookings page
    booking_page = driver.find_element(By.ID, "my-bookings-link")
    booking_page.click()
    # Wait for loading
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

    booking_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    
    for card in booking_cards:
        try:
            class_name = card.find_element(By.XPATH, ".//h3").text
            cards_info = card.find_element(By.XPATH, ".//p[1]").text
            if ("Tue" in cards_info or "Thu" in cards_info) and "6:00 PM" in cards_info:
                print(f"\t✓ Verified: {class_name}")
                verification_count += 1
        except NoSuchElementException:
            pass
    
    return verification_count

def booking_verification(total_tue_thu, verification_count):
    print("\n--- VERIFICATION RESULT ---")
    print(f"Expected: {total_tue_thu} booking(s)")
    print(f"Found: {verification_count} booking(s)")
    diff = total_tue_thu - verification_count
    if diff == 0:
        print("✅ SUCCESS: All bookings verified!")
    else:
        print(f"❌ MISMATCH: Missing {diff} bookings")

verification_count = retry(get_my_bookings, description="to get my booking")
booking_verification(total_tue_thu, verification_count)