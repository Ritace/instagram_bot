import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-data-dir=instagram")
# Create a WebDriver object.
driver = webdriver.Chrome(options=chrome_options)
# Set the WebDriver object's executable_path property to the path of the Selenium driver you want to use.
driver.executable_path = '/home/kali/projects/bot_for_place/chromedriver' 

# add cookies that was saved earlier instagram
driver.get('https://www.instagram.com/')
for cookie in driver.get_cookies(): 
    print(cookie)

time.sleep(5)
