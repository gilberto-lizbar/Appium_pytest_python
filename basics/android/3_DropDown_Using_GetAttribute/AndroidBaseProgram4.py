import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
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
time.sleep(3)
driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Forms"]').click()
time.sleep(3)

driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Dropdown"]').click()
time.sleep(2)

dropdown_options = driver.find_elements(By.ID,'android:id/text1')
print(len(dropdown_options))

for value in dropdown_options:
    ele_text = value.get_attribute("text")
    print(ele_text)
    if ele_text == "This app is awesome":
        print("desired option got displayed")
        value.click()
        break

time.sleep(2)
driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Dropdown"]').click()
time.sleep(2)
dropdown_options = driver.find_elements(By.ID,'android:id/text1')

for i in range(len(dropdown_options)):
    ele_text = dropdown_options[i].get_attribute("text")
    print(ele_text)
    if ele_text == "Appium is awesome":
        print("desired option got displayed")
        dropdown_options[i].click()
        break

time.sleep(3)

driver.quit()
