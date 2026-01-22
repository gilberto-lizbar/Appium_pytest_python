import time

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy

# Define Desired Capabilities in a dictionary

desired_caps = dict(
    # *****Capabilities for simulator phone*****
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
    autoAcceptAlerts=True,
    #fullReset=True,
    #noReset=False
)

# To establish a session with iOS you need to create an instant of XCUITestOptions
capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
time.sleep(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Sign up').click()
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter email address']").send_keys("gilberto.lizbar@gmail.com")
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter password']").send_keys("Gilcarjuan$1725")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue").click()
time.sleep(3)

driver.quit()
