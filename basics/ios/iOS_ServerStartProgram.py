import time
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

# Define Desired Capabilities in a dictionary
desired_caps = dict(
    automationName='XCUITest',
    deviceName='iPhone 15 Pro',
    platformName='iOS',
    platformVersion='17.4',
    app="/Users/gilberto.barraza/Desktop/Repo_Cursos/Courses_Resources/Appium_Selenium_Python/"
        "AppiumPython/app/iOS/Verve.app",
    udid='9B92B773-1F84-4CB2-8551-E821283E99CE',
    wdaLocalPort=8101,
    usePrebuiltWDA=True,
    wdaLaunchTimeout=30000,
    showXcodeLog=True,
    autoAcceptAlerts=True
)

appium_service = AppiumService()
appium_service.start()
print(f"Appium running: {appium_service.is_running}")
print(f"Appium listening: {appium_service.is_listening}")

# To establish a session with android you need to create an instant of UIAutomator2Options
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
time.sleep(3)
driver.implicitly_wait(10)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I already have an account").click()
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter email address']").send_keys("gilberto.lizbar@gmail.com")
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter password']").send_keys("Gilcarjuan$1725")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue").click()
time.sleep(5)
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter username']").send_keys("GilbertoLB")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "unSelected").click()
time.sleep(1)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign up").click()
driver.quit()

appium_service.stop()
