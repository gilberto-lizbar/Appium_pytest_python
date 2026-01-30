import time

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture(scope='function')
def setup_function(request):
    global driver
    global appium_service

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
        usePrebuiltWDA=False,
        wdaLaunchTimeout=30000,
        showXcodeLog=True,
        autoAcceptAlerts=True
    )
    appium_service = AppiumService()
    appium_service.start()
    print("appium server start")
    print(f"Appium running: {appium_service.is_running}")
    print(f"Appium listening: {appium_service.is_listening}")

    # To establish a session with android you need to create an instant of UIAutomator2Options
    capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    time.sleep(3)
    driver.implicitly_wait(10)
    request.node.driver = driver

    yield
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
def test_demo1():
    print("Execute this test to verify appium setup and teardown functions")
    text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Views").__getattribute__("text")
    print("********", text)

