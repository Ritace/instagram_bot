from appium import webdriver

def main():
  # Create an Appium session
  driver = webdriver.Remote("http://localhost:4726/wd/hub", desired_capabilities={
    "platformName": "Android",
    "deviceName": "Android emulator",
   "automationName": "UiAutomator2"
  })

  # Find the "Hello, world!" text
  element = driver.find_element_by_xpath("//*[@text='Hello, world!']")

  # Click on the "Hello, world!" text
  element.click()

  # Quit the Appium session
  driver.quit()

if __name__ == "__main__":
  main()
