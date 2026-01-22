import time

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

# Define Desired Capabilities in a dictionary

desired_caps = dict(
    # *****Capabilities for simulator phone*****
    automationName='XCUITest',
    deviceName='iPhone 15 Pro',
    platformName='iOS',
    platformVersion='17.4',
    app="/Users/gilberto.barraza/Library/Developer/Xcode/DerivedData/"
        "UIKitCatalog-ffzctqjqzsaewngteseolenbqayj/Build/Products/Debug-iphonesimulator/"
        "UIKitCatalog.app",
    udid='9B92B773-1F84-4CB2-8551-E821283E99CE',
    wdaLocalPort=8101,
    usePrebuiltWDA=True,
    wdaLaunchTimeout=30000,
    showXcodeLog=True,
    autoAcceptAlerts=True
)

# To establish a session with iOS you need to create an instant of XCUITestOptions
capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

time.sleep(3)
driver.implicitly_wait(10)

screen_size = driver.get_window_size()
start_x = int(screen_size['width']/2)
start_y = int(screen_size['height'] * 0.8)
end_y = int(screen_size['height'] * 0.2)

actions = ActionChains(driver)
pointer = PointerInput(interaction.POINTER_TOUCH,'finger')
action_builder = ActionBuilder(driver, mouse=pointer)

action_builder.pointer_action.move_to_location(x=start_x, y=start_y)
action_builder.pointer_action.pointer_down()
action_builder.pointer_action.move_to_location(x=start_x, y=end_y)
action_builder.pointer_action.pointer_up()

actions.w3c_actions = action_builder

actions.perform()

time.sleep(9)
driver.quit()
