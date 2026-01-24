import time

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture(scope='module')
def setup():
    print("DB connection start")

    yield
    print("DB connection closed")


@pytest.fixture(scope='function')
def before_Each_function():
    print("appium server start")
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
        autoAcceptAlerts=True
    )

    appium_service = AppiumService()
    appium_service.start()
    print(f"Appium running: {appium_service.is_running}")
    print(f"Appium listening: {appium_service.is_listening}")

    # To establish a session with android you need to create an instant of UIAutomator2Options
    capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    time.sleep(3)
    driver.implicitly_wait(10)
    # The 'yield' provides the driver to the test and pauses here
    yield driver

    # Teardown: runs after the test finishes
    print("\nStopping Appium server and closing driver...")
    try:
        driver.quit()
    except Exception as e:
        print("Exception during driver.quit():", e)
    appium_service.stop()


@pytest.mark.usefixtures("setup", "before_Each_function")
def test_hard_assertion(before_Each_function):
    # setup_driver is the 'driver' object yielded by the fixture
    driver = before_Each_function
    time.sleep(15)
    # with hard assertion , if the assertion got failed then script itself is stopping there itself# time.sleep(1)
    text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Views").__getattribute__("text")
    print("********", text)
    assert "Alert" in text


def test_hard_assertion2(setup, before_Each_function):
    # The Python statement assert False immediately raises an AssertionError
    assert False, "default failed"
    print("This line should not be printed")


# ******************************
def test_soft_assertion(setup, before_Each_function):
    soft_assert = SoftAssert()
    try:
        driver = before_Each_function
        text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Views").__getattribute__("text")
        soft_assert.check("Gilberto" in text, f"Expected 'Alert Views' to be) in text, got: '{text}'")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Views").click()
        time.sleep(3)
    except Exception as e:
        print("Exception during test execution:", e)
        soft_assert.check(False, f"Exception during test execution: {e}")
    finally:
        soft_assert.assert_all()


class SoftAssert:
    def __init__(self):
        self.errors = []

    def check(self, condition, msg):
        """Record msg if condition is False."""
        if not condition:
            self.errors.append(msg)

    def assert_all(self):
        """Raise a combined AssertionError if any checks failed."""
        if self.errors:
            raise AssertionError("Soft assertion failures:\n" + "\n".join(f"- {m}" for m in self.errors))
