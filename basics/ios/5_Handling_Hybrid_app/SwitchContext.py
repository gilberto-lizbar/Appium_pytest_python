import time

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

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
    autoAcceptAlerts=True
)

# To establish a session with iOS you need to create an instant of XCUITestOptions
capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign up").click()
driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="Continue with Google"]').click()
time.sleep(2)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue").click()
time.sleep(8)

contexts = driver.contexts
for context in contexts:
    print(context)
    if context.startswith("WEBVIEW"):
        driver.switch_to.context(context)
        break

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("gilberto.lizbar@gmail.com")
time.sleep(3)

driver.quit()
