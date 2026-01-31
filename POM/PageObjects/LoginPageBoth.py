from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from POM.Utils.MobileActions import MobileActions


class LoginPageBoth(MobileActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Detect platform once
        self.platform = self.driver.capabilities.get('platformName', '').lower()

        # Define Locators for both platforms
        self._locators = {
            "have_account": {
                "ios": (AppiumBy.ACCESSIBILITY_ID, "I already have an account"),
                "android": (AppiumBy.ID, "com.app:id/btn_have_account")
            },
            "username": {
                "ios": (By.XPATH, "//*[@value='Enter email address']"),
                "android": (By.CLASS_NAME, "android.widget.EditText")
            },
            "password": {
                "ios": (By.XPATH, "//*[@value='Enter password']"),
                "android": (By.XPATH, "//android.widget.EditText[@text='Password']")
            },
            "continue": {
                "ios": (AppiumBy.ACCESSIBILITY_ID, "Continue"),
                "android": (AppiumBy.ID, "com.app:id/submit")
            }
        }

    def get_locator(self, name):
        """Helper to fetch the correct locator based on current platform"""
        return self._locators[name][self.platform]

    def login(self, username, password):
        # Use the helper to get the platform-specific tuple
        self.wait.until(EC.element_to_be_clickable(self.get_locator("have_account"))).click()
        self.driver.find_element(*self.get_locator("username")).send_keys(username)
        self.driver.find_element(*self.get_locator("password")).send_keys(password)
        self.driver.find_element(*self.get_locator("continue")).click()
