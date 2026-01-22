import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
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
driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Login']/android.widget.TextView").click()
time.sleep(3)

obj = driver.find_element(By.XPATH, "//*[@text='Sign up']")

loc = obj.location
x_cor = loc['x']
y_cor = loc['y']

print(x_cor)
print(y_cor)

dim = obj.size
wid = dim['width']
hei = dim['height']

print(wid)
print(hei)

center_x = x_cor + (wid / 2)
center_y = y_cor + (hei / 2)

print(center_x)
print(center_y)

driver.quit()
