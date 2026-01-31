import base64
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium.options.ios import XCUITestOptions
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


# << ***************Test Reports Configuration On Failure***************
@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    # Handle both old and new pytest versions
    if hasattr(outcome, 'get_result'):
        rep = outcome.get_result()
    else:
        rep = outcome  # pytest 9.x returns the report directly
    setattr(item, "rep_" + rep.when, rep)
    return rep


# ***************Test Reports Configuration On Failure*************** >>

@pytest.fixture(scope='function')
def setup_function(request):
    global driver
    global appium_service
    appium_service = AppiumService()
    appium_service.start()
    print("appium server start")
    print(f"Appium running: {appium_service.is_running}")
    print(f"Appium listening: {appium_service.is_listening}")

    # Define Desired Capabilities in a dictionary
    desired_caps = dict(
        # *****Capabilities for simulator phone*****
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
        autoAcceptAlerts=True
    )

    # To establish a session with android you need to create an instant of UIAutomator2Options
    capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    time.sleep(3)
    driver.implicitly_wait(10)

    # --- START RECORDING ---
    print("Starting screen recording...")
    driver.start_recording_screen(
        # video_type='libx264',  # Change from 'mpeg4' to 'libx264'
        video_quality='medium',
        time_limit='180',
        # fps=30  # 30 fps is more standard for playback
    )

    yield driver
    # <<****log_on_failure****
    # --- STOP RECORDING AND PROCESS ---
    video_raw = driver.stop_recording_screen()

    item = request.node
    # If the test failed, attach both Screenshot and Video to Allure
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        # Attach Screenshot
        allure.attach(driver.get_screenshot_as_png(), name="failure_screenshot", attachment_type=AttachmentType.PNG)

        # Decode and Attach Video
        allure.attach(base64.b64decode(video_raw), name="failure_video", attachment_type=AttachmentType.MP4)
        print("Test failed: Screenshot and Video attached to report.")
    # ****log_on_failure****>>

    # <<****closing driver****
    if 'driver' in globals() and driver:
        try:
            print("Closing driver session...")
            driver.quit()
        except Exception as e:
            print(f"Error quitting driver: {e}")
    else:
        print("Driver was not initialized; skipping driver.quit()")
    # <<****closing driver****

    # <<****stopping appium service****
    # 2. Safely stop the Appium Service
    if 'appium_service' in globals() and appium_service:
        try:
            if appium_service.is_running:
                print("Stopping Appium server...")
                appium_service.stop()
        except Exception as e:
            print(f"Error stopping Appium service: {e}")

    print("[Teardown] Cleanup complete.")
