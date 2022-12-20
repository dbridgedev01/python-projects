from selenium import webdriver

# import statement for getting KEY Constants
from selenium.webdriver.common.keys import Keys

import config
import time

# Specify the path for chrome web driver [http://chromedriver.chromium.org/downloads]
CHROME_PATH = config.CHROME_PATH

# Values for Email and Password, change respectively.
EMAIL = config.EMAIL
PASSWORD = config.PASSWORD

course_url = input("Enter URL: ")

# Selecting the browser and specifying the respective driver location.
driver = webdriver.Chrome(executable_path=CHROME_PATH)

# To open the website
driver.get(course_url)

# Selecting the respective HTML elements to perform the desired action.
"""
If there is an error while selecting and despite specifying the correct elements,
increase the sleep time. This is happening due to a network latency.
"""
# For further understanding of element selection, read [https://selenium-python.readthedocs.io/locating-elements.html]
sign_in_button = driver.find_element_by_css_selector(".enterprise-interstitial__sign-in-btn")
time.sleep(1)
sign_in_button.click()

time.sleep(1)

email = driver.find_element_by_name("email")
# Sending the stored EMAIL to the Text Field.
email.send_keys(EMAIL)
continue_button = driver.find_element_by_id("auth-id-button")
time.sleep(1)
continue_button.click()

password = driver.find_element_by_id("password")
# Sending the stored PASSWORD to the Text Field.
password.send_keys(PASSWORD)
continue_button = driver.find_element_by_css_selector(".login__form_action_container button")
time.sleep(1)
continue_button.click()

time.sleep(2)
arrow_click = driver.find_element_by_css_selector('body')

# Indefinite Loop, stop the execution once the course is completed.
while True:
    time.sleep(1)
#   Using the Key Constant from Keys Class (imported)
    arrow_click.send_keys(Keys.ARROW_RIGHT)
