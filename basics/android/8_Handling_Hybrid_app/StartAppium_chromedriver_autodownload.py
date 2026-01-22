import time
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

# Node.js PATH

# type in terminal: which node
# /Users/gilberto.barraza/.nvm/versions/node/v20.19.5/bin/node
node_bin_path = '/Users/gilberto.barraza/.nvm/versions/node/v20.19.5/bin'
os.environ['PATH'] = f"{node_bin_path}:{os.environ.get('PATH', '')}"

# Set Android SDK environment variables - Note: using ~/Library/Android/sdk
android_sdk_path = os.path.expanduser('~/Library/Android/sdk')
os.environ['ANDROID_HOME'] = android_sdk_path
os.environ['ANDROID_SDK_ROOT'] = android_sdk_path

# Platform-tools to PATH

# type in terminal: which adb
# /Users/gilberto.barraza/Library/Android/sdk/platform-tools/adb
platform_tools = os.path.join(android_sdk_path, 'platform-tools')
os.environ['PATH'] = f"{platform_tools}:{os.environ['PATH']}"

print(f"ANDROID_HOME: {os.environ['ANDROID_HOME']}")
print(f"ADB location: {platform_tools}/adb")
print(f"ADB exists: {os.path.exists(os.path.join(platform_tools, 'adb'))}")

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
    appWaitDuration=30000,
)

appium_service = AppiumService()
# Allow appium autodownload chrome driver
appium_service.start(args=['--allow-insecure', 'uiautomator2:chromedriver_autodownload'])
print(f"Appium running: {appium_service.is_running}")
print(f"Appium listening: {appium_service.is_listening}")

# To establish a session with android you need to create an instant of UIAutomator2Options
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
time.sleep(3)

driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Webview"]/android.widget.TextView').click()
time.sleep(4)

contexts = driver.contexts
for context in contexts:
    print(context)

driver.switch_to.context("WEBVIEW_com.wdiodemoapp")
driver.find_element(By.XPATH, "//button[@class='DocSearch DocSearch-Button']").click()

time.sleep(3)
driver.quit()

