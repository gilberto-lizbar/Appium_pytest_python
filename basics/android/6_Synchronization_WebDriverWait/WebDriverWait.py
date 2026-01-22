import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Define Desired Capabilities in a dictionary

desired_caps = dict(
    automationName='UiAutomator2',
    deviceName='Galaxy A03s',
    platformName='Android',
    platformVersion='13',
    app='/Users/gilberto.barraza/Desktop/Repo_Cursos/Courses_Resources/Appium_Selenium_Python/'
        'AppiumPython/app/Android/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk',
    app_package='com.swaglabsmobileapp',
    app_activity='com.swaglabsmobileapp.MainActivity',
    # Add these capabilities
    autoGrantPermissions=True,  # Automatically grants all requested permissions to the app when it's installed.
    noReset=False,  # App is reinstalled before the session, clearing all data (cache, login state, settings)
    # noReset=True,  # App keeps its state from the previous session (stays logged in, preserves data)
    fullReset=False,  # (default): Only reinstalls the app
    # fullReset=True,  # Removes the app completely, clears all data, and performs a clean install
    appWaitActivity='*',  # Wait for any activity
    appWaitDuration=30000,  # Wait up to 30 seconds for app to start
)
# To establish a session with android you need to create an instant of UIAutomator2Options
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

time.sleep(5)
# Global Timeout when attempting to find elements that are not immedaitely available
driver.implicitly_wait(15)

screen_size = driver.get_window_size()
start_x = int(screen_size['width'] / 2)
start_y = int(screen_size['height'] * 0.8)
end_y = int(screen_size['height'] * 0.2)

actions = ActionChains(driver)
pointer = PointerInput(interaction.POINTER_TOUCH, 'finger')
action_builder = ActionBuilder(driver, mouse=pointer)

action_builder.pointer_action.move_to_location(x=start_x, y=start_y)
action_builder.pointer_action.pointer_down()
action_builder.pointer_action.move_to_location(x=start_x, y=end_y)
action_builder.pointer_action.pointer_up()

actions.w3c_actions = action_builder

actions.perform()

# Declare a webdriverwait  - Explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located
           ((By.XPATH, "//*[@text='standard_user']")))

# Fluent wait is an improved explicit wait
wait = WebDriverWait(driver,
                     timeout=20,  # Maximum wait time in seconds
                     poll_frequency=5,  # Check every 5 second
                     ignored_exceptions=[NoSuchElementException,
                                         ElementNotVisibleException,
                                         ElementNotSelectableException])

wait.until(expected_conditions.visibility_of_element_located
           ((By.XPATH, "//*[@text='secret_sauce']")))

time.sleep(5)

driver.quit()
