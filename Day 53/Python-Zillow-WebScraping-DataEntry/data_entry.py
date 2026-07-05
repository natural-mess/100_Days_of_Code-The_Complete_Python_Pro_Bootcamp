from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DataEntry:
    def __init__(self, url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.form_url = url

    def _submit_form(self):
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'l4V7wb')
        submit_btn.click()

    def _keep_filling_form(self):
        new_response = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
        new_response.click()

    def fill_form(self, links, prices, addresses):
        self.driver.get(f"{self.form_url}")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "o3Dpx")))

        for i in range(len(addresses)):
            address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(addresses[i])

            price_input = self.driver.find_element(By.XPATH,
                                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(prices[i])

            link_input = self.driver.find_element(By.XPATH,
                                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(links[i])

            self._submit_form()
            self._keep_filling_form()

test_links = ['https://www.zillow.com/b/747-geary-street-oakland-ca-CYzGVt/']
test_addresses = ['747 Geary Street, 747 Geary St, Oakland, CA 94609']
test_prices = ['$2,895']

if __name__ == "__main__":
    test_url = "https://forms.gle/f8pE67gS2bKNBL2J6"
    test_driver = DataEntry(test_url)
    test_driver.fill_form(test_links, test_prices, test_addresses)