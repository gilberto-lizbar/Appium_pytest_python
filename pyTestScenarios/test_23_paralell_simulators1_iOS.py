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


@pytest.fixture(params=['device1', 'device2'], scope='function')
def setup_function(request):
    # DEVICE 1
    # Appium Service is not declared in this test: start the service in terminal: appium -p 4723

    # DEVICE 2
    # Appium Service is not declared in this test: start the service in terminal: appium -p 4724
    if request.param == 'device1':
        server_url = 'http://127.0.0.1:4723'
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

    elif request.param == 'device2':
        server_url = 'http://127.0.0.1:4724'
        # Define Desired Capabilities in a dictionary
        desired_caps = dict(
            # *****Capabilities for simulator phone*****
            automationName='XCUITest',
            deviceName='iPhone 15 Pro Max',
            platformName='iOS',
            platformVersion='17.4',
            app="/Users/gilberto.barraza/Desktop/Repo_Cursos/Courses_Resources/Appium_Selenium_Python/"
                "AppiumPython/app/iOS/Verve.app",
            udid='336D6536-AB5D-49CE-A85E-48DF703DB799',
            wdaLocalPort=8102,
            usePrebuiltWDA=True,
            wdaLaunchTimeout=30000,
            showXcodeLog=True,
            autoAcceptAlerts=True
        )
    else:
        appium_port = ""
        server_url = ""
        desired_caps = {}

    # To establish a session with android you need to create an instant of UIAutomator2Options
    capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
    # driver = webdriver.Remote('http://127.0.0.1:4724', options=capabilities_options)
    driver = webdriver.Remote(server_url, options=capabilities_options)
    time.sleep(3)
    driver.implicitly_wait(10)

    request.node.driver = driver
    yield driver
    # <<****log_on_failure****
    item = request.node
    # Check if rep_call attribute exists and then check if it failed
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="image1", attachment_type=AttachmentType.PNG)
    # ****log_on_failure****>>

    # <<****closing driver****
    if driver:
        try:
            print("Closing driver session...")
            driver.quit()
        except Exception as e:
            print(f"Error quitting driver: {e}")
    else:
        print("Driver was not initialized; skipping driver.quit()")
    # <<****closing driver****


# @pytest.mark.usefixtures("setup_function")
@pytest.mark.parametrize("test_list_item", test_list)  # Extract test_list and attached to test_list_item
# Send test_list_item as an argument of test method to have access to test_list_item data
def test_signUp_to_app(setup_function, test_list_item):
    #driver = setup_function
    print("Sign Up test")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I already have an account").click()
    driver.find_element(AppiumBy.XPATH, "//*[@value='Enter email address']").send_keys(test_list_item["email"])
    driver.find_element(AppiumBy.XPATH, "//*[@value='Enter password']").send_keys(test_list_item["password"])
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue").click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, "//*[@value='Enter username']").send_keys(test_list_item["username"])
    # allure.attach(driver.get_screenshot_as_png(), name='image', attachment_type=AttachmentType.PNG)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "unSelected").click()
    time.sleep(1)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign up").click()
