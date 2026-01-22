import time
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

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
    autoGrantPermissions=True,
    noReset=False,
    fullReset=False,
    appWaitActivity='*',
    appWaitDuration=30000
)

appium_service = AppiumService()
appium_service.start()
print(f"Appium running: {appium_service.is_running}")
print(f"Appium listening: {appium_service.is_listening}")

# Allow appium autodownload chrome driver
appium_service.start(args=['--allow-insecure', 'uiautomator2:chromedriver_autodownload'])
# To establish a session with android you need to create an instant of UIAutomator2Options
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

time.sleep(5)
driver.quit()

appium_service.stop()
