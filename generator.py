import json
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
MOST LIKELY DEPRECATED
USE V2
"""
class GeneratorService(object):
    def cookie(self, data=None):
        # Check if the JSON file exists
        json_filename = "./data.json"
        if not os.path.exists(json_filename):
            # Create the JSON file if it doesn't exist
            with open(json_filename, "w") as file:
                json.dump({}, file)

        # Data to be written into the JSON file

        # Read existing JSON data (if any)
        existing_data = {}
        with open(json_filename, "r") as file:
            existing_data = json.load(file)

        if data:
            existing_data.update(data)

            with open(json_filename, "w") as file:
                json.dump(existing_data, file, indent=4)
        return existing_data

    def get_text(self, elem):
        """
        Get Selenium element text

        Args:
            curElement (WebElement): selenium web element
        Returns:
            str
        Raises:
        """
        # # for debug
        # elementHtml = curElement.get_attribute("innerHTML")
        # print("elementHtml=%s" % elementHtml)

        elementText = elem.text  # sometime NOT work
        a = elem.get_attribute("innerText")
        b = elem.get_attribute("textContent")
        if not elementText:
            elementText = elem.get_attribute("innerText")

        if not elementText:
            elementText = elem.get_attribute("textContent")

        # print("elementText=%s" % elementText)
        return elementText

    def extract_web_auth_data(self):
        query = input('enter your query: ')
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        options = webdriver.ChromeOptions()
        path_to_extension = '/Users/enigma/Projects/lead-generator/ext'
        options.add_argument('load-extension=' + path_to_extension)
        options.add_argument(f'--user-agent={user_agent}')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        service = Service(executable_path=ChromeDriverManager().install())
        dict_headers = self.cookie()
        if dict_headers:
            for key, value in dict_headers.items():
                options.add_argument(f"--header={key}: {value}")
        driver = webdriver.Chrome(service=service, options=options)
        actions = ActionChains(driver)

        driver.get(
            'https://www.linkedin.com/search/results/all/?keywords=(%22Business%20Case%20Service%22%20OR%20%22Disease%20Research%22)%20AND%20%22pharma%22&origin=HISTORY&sid=%40Lv')
        try:
            user_login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/p/a')
            user_login.click()
            wait = WebDriverWait(driver, 10)  # Maximum wait time in seconds
            wait.until(EC.presence_of_element_located(('id', 'username')))
            driver.find_element('id', 'username').send_keys('') #EMAIL
            driver.find_element('id', 'password').send_keys('') #PASSWORD
            driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
            time.sleep(5)
            search = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
            search.clear()
            search.send_keys(f'{query}')
            search.click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[text() = "See all results"]').click()
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[text() = "Companies"]').click()
            time.sleep(5)
            # Iterate through each li element and find the nested a element
            counter = 0
            for idx, li in enumerate(driver.find_elements(By.CLASS_NAME, "reusable-search__result-container"), start=1):
                try:
                    a_element = li.find_element(By.CLASS_NAME, "app-aware-link")
                    actions.move_to_element(a_element).key_down(Keys.COMMAND).click(a_element).key_up(
                        Keys.COMMAND).perform()
                    time.sleep(5)
                    driver.switch_to.window(driver.window_handles[idx - counter])
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, "a.ember-view.org-top-card-summary-info-list__info-item").click()
                    time.sleep(5)
                    try:
                        driver.find_element(By.CLASS_NAME, 'KLM_2726252_POPUP_OPEN').click()
                        time.sleep(5)
                        driver.find_element(By.CLASS_NAME, 'bind__837362622').click()
                    except:
                        driver.refresh()
                        time.sleep(5)
                        driver.find_element(By.CLASS_NAME, 'KLM_2726252_POPUP_OPEN').click()
                        time.sleep(5)
                        driver.find_element(By.CLASS_NAME, 'bind__837362622').click()

                    driver.switch_to.window(driver.window_handles[0])
                except Exception as e:
                    print(e)
                    driver.close()
                    counter += 1
                    driver.switch_to.window(driver.window_handles[0])
                    continue

        except Exception as e:
            driver.close()
            print(e)
        input("Press Enter to close the browser...")
        driver.quit()

