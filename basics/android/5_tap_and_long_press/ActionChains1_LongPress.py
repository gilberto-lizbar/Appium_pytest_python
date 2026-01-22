import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

# Define Desired Capabilities in a dictionary

desired_caps = dict(
    automationName='UiAutomator2',
    deviceName='Galaxy A03s',
    platformName='Android',
    platformVersion='13',
    app='/Users/gilberto.barraza/Desktop/Repo_Cursos/Courses_Resources/Appium_Selenium_Python/'
        'AppiumPython/app/Android/ApiDemo_1.1_Apkpure.apk',
    app_package='demo.fun.com.apis',
    app_activity='demo.fun.com.apis.ApiDemos',
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
driver.implicitly_wait(15)

driver.find_element(By.XPATH, "//*[@text='Views']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@text='Expandable Lists']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@text='1. Custom Adapter']").click()
time.sleep(2)


actions = ActionChains(driver)
pointer = PointerInput(interaction.POINTER_TOUCH, 'touch')
action_builder = ActionBuilder(driver, mouse=pointer)

LongPress = driver.find_element(By.XPATH, "//*[@text='People Names']")

action_builder.pointer_action.move_to(LongPress).pointer_down().pause(3).pointer_up()

actions.w3c_actions = action_builder
actions.perform()

time.sleep(5)

driver.quit()
