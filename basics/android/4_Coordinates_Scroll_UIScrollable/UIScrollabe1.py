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

time.sleep(10)

driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//*[@text='Views']").click()

ui_scrollable = ('new UiScrollable(new UiSelector().scrollable(true))'
                 '.scrollIntoView(new UiSelector().text("WebView"))')

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ui_scrollable)
driver.find_element(By.XPATH, "//*[@text='WebView']").click()

time.sleep(5)

driver.quit()
