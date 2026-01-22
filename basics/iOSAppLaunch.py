import time

from appium import webdriver
from appium.options.ios import XCUITestOptions

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

    # *****Physical Device Capabilities required (Apple dev account is required)*****
    # automationName='XCUITest',
    # deviceName='Gilberto Lizarraga Barraza´s iPhone',
    # platformName='iOS',
    # platformVersion='18.6.2',  # physical device
    # app='/Users/gilberto.barraza/Library/Developer/Xcode/DerivedData/'
    #    'UIKitCatalog-ffzctqjqzsaewngteseolenbqayj/Build/Products/Debug-iphoneos/UIKitCatalog.app',
    # bundleId='com.gilberto-lizarraga.UIKitCatalog',  # Your app's bundle ID
    # xcodeOrgId='GTDX8WH954',  # Replace with your Team ID security
    # #Type this command in terminal for xcodeOrgId: security find-identity -v -p codesigning | grep "Apple Development"
    # xcodeSigningId='iPhone Developer',
    # updatedWDABundleId='com.gilberto-lizarraga.WebDriverAgentRunner',
    # udid='00008120-0012591024434032'  # physical device
)

# To establish a session with iOS you need to create an instant of XCUITestOptions
capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
capabilities_options.set_capability('wdaLocalPort', 8101)  # or any free port
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

# --- Essential Additions for Stability ---
# Forces the simulator to wait for the WDA to be ready
capabilities_options.set_capability('appium:wdaLaunchTimeout', 30000)
# Shows the Xcode logs in your Appium server console (crucial for debugging Code 70)
capabilities_options.set_capability('appium:showXcodeLog', True)
# Automatically handles "Allow Notifications" or "Use Location" popups
capabilities_options.set_capability('appium:autoAcceptAlerts', True)
# Ensures the simulator starts fresh if needed
capabilities_options.set_capability('appium:fullReset', True)
capabilities_options.set_capability('appium:noReset', False)

time.sleep(5)
driver.quit()
