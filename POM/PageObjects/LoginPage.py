import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.Utils.MobileActions import MobileActions


class LoginPage(MobileActions):

    def __init__(self, driver):  # Add driver as an argument of constructor to force whoever
        # call page class to activate the driver
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 10-second timeout
        self.have_account_btn = (AppiumBy.ACCESSIBILITY_ID, "I already have an account")
        self.username_field = (By.XPATH, "//*[@value='Enter email address']")  # packaging tuple
        self.password_field = (By.XPATH, "//*[@value='Enter password']")
        self.continue_btn = (AppiumBy.ACCESSIBILITY_ID, "Continue")

    def login(self, username, password):
        # self.username_input is recognized as 1 argument in driver.find_element(self.username_input)
        # find elements expects 2 arguments to works
        # to split original tupple (By.ID, "username") into 2 arguments you need to add *
        # before the variable like this: *self.username_input (packaging tuple)

        # self.driver.find_element(self.have_account_btn).click()  # does not work
        # self.driver.find_element(*self.have_account_btn).click() # works
        self.scroll_down()
        self.wait.until(expected_conditions.element_to_be_clickable(self.have_account_btn)).click()
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.continue_btn).click()
        self.driver.find_element(*self.password_field).send_keys(password)

