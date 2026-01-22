import datetime
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
    app="/Users/gilberto.barraza/Library/Developer/Xcode/DerivedData/"
        "UIKitCatalog-ffzctqjqzsaewngteseolenbqayj/Build/Products/Debug-iphonesimulator/"
        "UIKitCatalog.app",
    udid='9B92B773-1F84-4CB2-8551-E821283E99CE',
    wdaLocalPort=8101,
    usePrebuiltWDA=True,
    wdaLaunchTimeout=30000,
    showXcodeLog=True,
    autoAcceptAlerts=True,
)

# To establish a session with iOS you need to create an instant of XCUITestOptions
capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

time.sleep(3)
driver.implicitly_wait(10)
# date picker
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Picker View").click()
time.sleep(10)
driver.find_element(By.XPATH, "(//*[@type='XCUIElementTypePickerWheel'])[1]").send_keys('50')
driver.find_element(By.XPATH, "(//*[@type='XCUIElementTypePickerWheel'])[2]").send_keys('155')
driver.find_element(By.XPATH, "(//*[@type='XCUIElementTypePickerWheel'])[2]").send_keys('100')
#driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Friday 11 April").click()

time.sleep(1)
driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='UIKitCatalog']").click()

time.sleep(3)

driver.quit()
