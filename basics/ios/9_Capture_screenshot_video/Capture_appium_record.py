import base64
import os.path
import time

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

# Define Desired Capabilities in a dictionary

desired_caps = dict(
    automationName='XCUITest',
    deviceName='iPhone 15 Pro',
    platformName='iOS',
    platformVersion='17.4',
    app="/Users/gilberto.barraza/Desktop/Repo_Cursos/Courses_Resources/Appium_Selenium_Python/"
        "AppiumPython/app/iOS/Verve.app",
    udid='9B92B773-1F84-4CB2-8551-E821283E99CE',
    wdaLocalPort=8101,
    usePrebuiltWDA=True,
    wdaLaunchTimeout=30000,
    showXcodeLog=True,
    autoAcceptAlerts=True,
    # ... your other caps ...
    # useNewWDA=True,
    # This helps Appium find the homebrew binaries
    # processArguments={'env': {'PATH': '/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'}}
)

appium_service = AppiumService()
appium_service.start()
print(f"Appium running: {appium_service.is_running}")
print(f"Appium listening: {appium_service.is_listening}")

# To establish a session with android you need to create an instant of UIAutomator2Options
capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
time.sleep(10)
# Start Screen Recording
driver.start_recording_screen()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I already have an account").click()
driver.save_screenshot("/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/ios/records/capture1.png")
time.sleep(3)
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter email address']").send_keys("gilberto.lizbar@gmail.com")
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter password']").send_keys("test$1234")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue").click()
time.sleep(5)

driver.save_screenshot("/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/ios/records/capture2.png")
raw_data = driver.stop_recording_screen()
filepath = os.path.join("/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/ios/records/appiumVideo.mp4")

with open(filepath, "wb") as video:
    video.write(base64.b64decode(raw_data))

# <<****closing driver****
driver.quit()
print("Closing driver session...")

# <<****stopping appium service****
appium_service.stop()
print(f"Stopping Appium server on port ...")
