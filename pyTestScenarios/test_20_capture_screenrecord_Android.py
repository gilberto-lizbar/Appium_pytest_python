import base64
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

    # To establish a session with android you need to create an instant of UIAutomator2Options
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    time.sleep(3)
    driver.implicitly_wait(10)

    # --- START RECORDING ---
    print("Starting screen recording...")
    driver.start_recording_screen()

    yield
    # <<****log_on_failure****
    # --- STOP RECORDING AND PROCESS ---
    video_raw = driver.stop_recording_screen()

    item = request.node
    # If the test failed, attach both Screenshot and Video to Allure
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        # Attach Screenshot
        allure.attach(driver.get_screenshot_as_png(), name="failure_screenshot", attachment_type=AttachmentType.PNG)

        # Decode and Attach Video
        allure.attach(base64.b64decode(video_raw), name="failure_video", attachment_type=AttachmentType.MP4)
        print("Test failed: Screenshot and Video attached to report.")
    # ****log_on_failure****>>

    # <<****closing driver****
    if 'driver' in globals() and driver:
        try:
            print("Closing driver session...")
            driver.quit()
        except Exception as e:
            print(f"Error quitting driver: {e}")
    else:
        print("Driver was not initialized; skipping driver.quit()")
    # <<****closing driver****

    # <<****stopping appium service****
    # 2. Safely stop the Appium Service
    if 'appium_service' in globals() and appium_service:
        try:
            if appium_service.is_running:
                print("Stopping Appium server...")
                appium_service.stop()
        except Exception as e:
            print(f"Error stopping Appium service: {e}")

    print("[Teardown] Cleanup complete.")
    # ****stopping appium service****>>


#@pytest.mark.usefixtures("setup_function")
@pytest.mark.parametrize("test_list_item", test_list)  # Extract test_list and attached to test_list_item
# Send test_list_item as an argument of test method to have access to test_list_item data
def test_signUp_to_app(setup_function, test_list_item):
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
    driver.find_element(By.XPATH, '//*[@content-desc="No existing xpath"]').click()

