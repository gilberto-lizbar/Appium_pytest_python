import json
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

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
            automationName='UiAutomator2',
            deviceName='Pixel_4a_API_31',
            platformName='Android',
            platformVersion='12',
            app='/Users/gilberto.barraza/Desktop/Repo_Cursos/Courses_Resources/Appium_Selenium_Python/'
                'AppiumPython/app/Android/Android-NativeDemoApp-0.4.0.apk',
            app_package='com.wdiodemoapp',
            app_activity='com.wdiodemoapp.MainActivity',
            systemPort=8202,
            # Add these capabilities
            autoGrantPermissions=True,  # Automatically grants all requested permissions to the app when it's installed.
            noReset=False,  # App is reinstalled before the session, clearing all data (cache, login state, settings)
            # noReset=True,  # App keeps its state from the previous session (stays logged in, preserves data)
            fullReset=False,  # (default): Only reinstalls the app
            # fullReset=True,  # Removes the app completely, clears all data, and performs a clean install
            appWaitActivity='*',  # Wait for any activity
            appWaitDuration=30000  # Wait up to 30 seconds for app to start
        )

    elif request.param == 'device2':
        server_url = 'http://127.0.0.1:4724'
        # Define Desired Capabilities in a dictionary
        desired_caps = dict(
            automationName='UiAutomator2',
            deviceName='Galaxy A03s',
            platformName='Android',
            platformVersion='13',
            app='/Users/gilberto.barraza/Desktop/Repo_Cursos/Courses_Resources/Appium_Selenium_Python/'
                'AppiumPython/app/Android/Android-NativeDemoApp-0.4.0.apk',
            app_package='com.wdiodemoapp',
            app_activity='com.wdiodemoapp.MainActivity',
            systemPort=8201,
            # Add these capabilities
            autoGrantPermissions=True,  # Automatically grants all requested permissions to the app when it's installed.
            noReset=False,  # App is reinstalled before the session, clearing all data (cache, login state, settings)
            # noReset=True,  # App keeps its state from the previous session (stays logged in, preserves data)
            fullReset=False,  # (default): Only reinstalls the app
            # fullReset=True,  # Removes the app completely, clears all data, and performs a clean install
            appWaitActivity='*',  # Wait for any activity
            appWaitDuration=30000,  # Wait up to 30 seconds for app to start
        )

    else:
        server_url = ""
        desired_caps = {}

    # To establish a session with android you need to create an instant of UIAutomator2Options
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote(server_url, options=capabilities_options)
    time.sleep(3)
    driver.implicitly_wait(10)

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


# @pytest.mark.usefixtures("setup_function")
@pytest.mark.parametrize("test_list_item", test_list)  # Extract test_list and attached to test_list_item
# Send test_list_item as an argument of test method to have access to test_list_item data
def test_signUp_to_app(setup_function, test_list_item):
    driver = setup_function
    print("Sign Up test")
    driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Login"]/android.widget.TextView').click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@text='Sign up']").click()
    (driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="input-email"]')
     .send_keys("gilberto.lizbar@gmail.com"))
    (driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="input-password"]')
     .send_keys(test_list_item["email"]))
    (driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="input-repeat-password"]')
     .send_keys(test_list_item["password"]))
    driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="button-SIGN UP"]').click()

