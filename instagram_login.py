import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# create chrome options with userdatadir as instagram and adding to driver 
chrome_options = Options()
chrome_options.add_argument("user-data-dir=instagram")
# Create a WebDriver object.
driver = webdriver.Chrome(options=chrome_options)
# Set the WebDriver object's executable_path property to the path of the Selenium driver you want to use.
driver.executable_path = '/home/kali/projects/bot_for_place/chromedriver' 

# Navigate to the Reddit website.
driver.get('https://www.instagram.com/')

# Log in to Reddit.
username = 'rit.ace.thapa@gmail.com'
password = 'Killforweeds@13'

#wait until website gets loaded 
time.sleep(5)
#get the element with name="username"
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)
#get the button of type="submit"
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

time.sleep(10)
#check if login in successful

# get all cookies of browser and dump them using pickle

pickle.dump(driver.get_cookies(), open("instagram_cookies.pkl", "wb"))
# Find the r/place subreddit.
# # driver.find_element_by_link_text('r/place').click()

# Click on the "Place a pixel" button.
# driver.find_element_by_id('placeButton').click()

# Enter the coordinates of the pixel you want to place.
#x = 712 
#y = -255

#driver.find_element_by_id('placeX').send_keys(x)
#driver.find_element_by_id('placeY').send_keys(y)
#
## Click on the "Place pixel" button.
#driver.find_element_by_id('placeButton').click()

# Repeat steps 10 and 11 for each pixel you want to place.

# Quit the WebDriver object.
driver.quit()
