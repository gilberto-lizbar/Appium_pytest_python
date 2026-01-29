import base64
import os.path
import time
import subprocess
import signal

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

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
    # useNewWDA=True,
    # processArguments={'env': {'PATH': '/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'}}
)

appium_service = AppiumService()
appium_service.start()
print(f"Appium running: {appium_service.is_running}")
print(f"Appium listening: {appium_service.is_listening}")

capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

# Wait for app to fully load
time.sleep(10)

# Start native screen recording
#udid = '9B92B773-1F84-4CB2-8551-E821283E99CE'
udid = desired_caps["udid"]
video_path = "/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/ios/records/iOSNativeVideo.mp4"

# Start recording using xcrun simctl
recording_process = subprocess.Popen([
    'xcrun', 'simctl', 'io', udid, 'recordVideo',
    '--codec=h264',
    '--force',
    video_path
])
print(f"Native screen recording started (PID: {recording_process.pid})")
time.sleep(2)  # Give recording time to start

# Run your test
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I already have an account").click()
driver.save_screenshot("/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/ios/records/capture1.png")
time.sleep(3)
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter email address']").send_keys("gilberto.lizbar@gmail.com")
driver.find_element(AppiumBy.XPATH, "//*[@value='Enter password']").send_keys("test$1234")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue").click()
time.sleep(5)
driver.save_screenshot("/Users/gilberto.barraza/Desktop/Repo_Cursos/Appium_Python/basics/ios/records/capture2.png")

# Stop recording using xcrun simctl
if recording_process:
    print("Stopping screen recording...")
    recording_process.send_signal(signal.SIGINT)  # Send interrupt signal
    recording_process.wait(timeout=10)  # Wait for process to finish
    print(f"Video saved to {video_path}")
    if os.path.exists(video_path):
        print(f"Video file size: {os.path.getsize(video_path)} bytes")

# <<****closing driver****
driver.quit()
print("Closing driver session...")

# <<****stopping appium service****
appium_service.stop()
print(f"Stopping Appium server on port ...")
