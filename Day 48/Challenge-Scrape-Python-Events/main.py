from selenium import webdriver
from selenium.webdriver.common.by import By

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_dict = {}
event_date = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

# date_list = []
# for date in event_date:
#     date_list.append(date.get_attribute('datetime').split('T')[0])

# name_list = []
# for name in event_name:
#     name_list.append(name.text)

for i in range(len(event_date)):
    event_dict[i]={
        'date': event_date[i].get_attribute('datetime').split('T')[0],
        'name': event_name[i].text,
    }

print(event_dict)

# Closes Chrome
driver.quit()