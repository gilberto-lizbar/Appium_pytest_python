import base64
import os.path
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
time.sleep(10)
driver.start_recording_screen()
driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Login"]/android.widget.TextView').click()
time.sleep(3)
driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="input-email"]').send_keys("12345")
driver.save_screenshot("/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/android/records/capture1.png")
time.sleep(3)

# driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Forms"]').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Forms').click()
time.sleep(3)

driver.find_element(By.XPATH,'//android.widget.EditText[@content-desc="text-input"]').send_keys("1234")
# driver.find_element(By.XPATH,'//android.widget.Switch[@content-desc="switch"]').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'switch').click()
time.sleep(2)

driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Dropdown"]').click()
time.sleep(2)

driver.find_element(By.XPATH,"//*[@text='Appium is awesome']").click()

driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="button-Active"]').click()
time.sleep(2)
driver.find_element(By.ID,'android:id/button2').click()
driver.save_screenshot("/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/android/records/capture2.png")
raw_data = driver.stop_recording_screen()
filepath = os.path.join("/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/android/records/"
                        "captureVideo.mp4")

with open(filepath, "wb") as video:
    video.write(base64.b64decode(raw_data))

driver.quit()
