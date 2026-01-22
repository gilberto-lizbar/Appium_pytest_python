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
    #deviceName='Galaxy A03s',
    deviceName='Pixel_4_API_31',
    platformName='Android',
    #platformVersion='13',
    platformVersion='12',
    app_package='com.sec.android.app.camera',
    app_activity='com.sec.android.app.camera.Camera',
)
# To establish a session with android you need to create an instant of UIAutomator2Options
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
time.sleep(5)
print("started")

time.sleep(15)

driver.quit()




