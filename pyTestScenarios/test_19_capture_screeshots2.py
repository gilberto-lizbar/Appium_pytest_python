import json
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

test_data_path = 'test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]  # Storing in a list all content of 'data' key from json


@pytest.fixture(scope='function')
def setup_function(request):
    global driver
    global appium_service
    appium_service = AppiumService()
    appium_service.start()
    print("appium server start")
    print(f"Appium running: {appium_service.is_running}")
    print(f"Appium listening: {appium_service.is_listening}")

    # Define Desired Capabilities in a dictionary
    desired_caps = dict(
        # *****Capabilities for simulator phone*****
        automationName='XCUITest',
        deviceName='iPhone 15 Pro',
        platformName='iOS',
        platformVersion='17.4',
        # app="/Users/gilberto.barraza/Library/Developer/Xcode/DerivedData/"
        #     "UIKitCatalog-ffzctqjqzsaewngteseolenbqayj/Build/Products/Debug-iphonesimulator/"
        #     "UIKitCatalog.app",
        app="/Users/gilberto.barraza/Desktop/Repo_Cursos/Courses_Resources/Appium_Selenium_Python/"
            "AppiumPython/app/iOS/Verve.app",
        wdaLocalPort=8101,
        usePrebuiltWDA=True,
        wdaLaunchTimeout=30000,
        showXcodeLog=True,
        autoAcceptAlerts=True
    )

    # To establish a session with android you need to create an instant of UIAutomator2Options
    capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    time.sleep(3)
    driver.implicitly_wait(10)

    yield
    item = request.node
    # Check if rep_call attribute exists and then check if it failed
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="image1", attachment_type=AttachmentType.PNG)

    if 'driver' in globals() and driver:
        try:
            print("Closing driver session...")
            driver.quit()
        except Exception as e:
            print(f"Error quitting driver: {e}")
    else:
        print("Driver was not initialized; skipping driver.quit()")

    # 2. Safely stop the Appium Service
    if 'appium_service' in globals() and appium_service:
        try:
            if appium_service.is_running:
                print("Stopping Appium server...")
                appium_service.stop()
        except Exception as e:
            print(f"Error stopping Appium service: {e}")

    print("[Teardown] Cleanup complete.")


@pytest.mark.usefixtures("setup_function")
@pytest.mark.parametrize("test_list_item", test_list)  # Extract test_list and attached to test_list_item
# Send test_list_item as an argument of test method to have access to test_list_item data
def test_signUp_to_app(test_list_item):
    print("Sign Up test")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I already have an account").click()
    driver.find_element(AppiumBy.XPATH, "//*[@value='Enter email address']").send_keys(test_list_item["email"])
    driver.find_element(AppiumBy.XPATH, "//*[@value='Enter password']").send_keys(test_list_item["password"])
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue").click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, "//*[@value='Enter username']").send_keys(test_list_item["username"])
    #allure.attach(driver.get_screenshot_as_png(), name='image', attachment_type=AttachmentType.PNG)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "unSelected").click()
    time.sleep(1)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign up").click()
