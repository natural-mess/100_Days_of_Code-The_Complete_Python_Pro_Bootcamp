from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS selectors
article_count = driver.find_elements(By.CSS_SELECTOR, value='#articlecount a')
# print(article_count[1].text)
# article_count[1].click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

# Find the "Search" <input> by Name
# search_button = driver.find_element(By.CSS_SELECTOR, value='#p-search .search-toggle')
# search_button.click()
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input by Selenium
search.send_keys("Python", Keys.ENTER)

# Closes Chrome
# driver.quit()