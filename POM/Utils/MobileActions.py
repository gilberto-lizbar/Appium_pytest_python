from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait


class MobileActions:

    def __init__(self, driver):  # Add driver as an argument of constructor to force whoever
        # call page class to activate the driver
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 10-second timeout
        self.platform = self.driver.capabilities['platformName'].lower()

    # *******************************************************+
    # **********           SCROLLS                  **********
    # *******************************************************+
    def scroll_down(self):
        screen_size = self.driver.get_window_size()
        start_x = int(screen_size['width'] / 2)
        start_y = int(screen_size['height'] * 0.8)
        end_y = int(screen_size['height'] * 0.2)

        actions = ActionChains(self.driver)
        pointer = PointerInput(interaction.POINTER_TOUCH, 'finger')
        action_builder = ActionBuilder(self.driver, mouse=pointer)

        action_builder.pointer_action.move_to_location(x=start_x, y=start_y)
        action_builder.pointer_action.pointer_down()
        action_builder.pointer_action.move_to_location(x=start_x, y=end_y)
        action_builder.pointer_action.pointer_up()

        actions.w3c_actions = action_builder

        actions.perform()

    def scroll_to_text(self, text, contains=False):
        """Scrolls until the element with the specific text is visible."""
        if self.platform == 'android':
            selector = f'new UiSelector().text("{text}")' if not contains else f'new UiSelector().textContains("{text}")'
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView({selector})'
            )
        else:
            # iOS: If partial match is needed, we'd find element first, else use 'name'
            self.driver.execute_script('mobile: scroll', {
                'direction': 'down',
                'name': text
            })

    def scroll_to_accessibility_id(self, accessibility_id):
        """Scrolls to an element using Content Desc (Android) or Accessibility ID (iOS)."""
        if self.platform == 'android':
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("{accessibility_id}"))'
            )
        else:
            self.driver.execute_script('mobile: scroll', {
                'direction': 'down',
                'name': accessibility_id
            })

    def scroll_to_beginning(self):
        """Scrolls to the very top of the scrollable view."""
        if self.platform == 'android':
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)'
            )
        else:
            self.driver.execute_script('mobile: scroll', {'direction': 'up'})

    def scroll_to_end(self):
        """Scrolls to the very bottom of the scrollable view."""
        if self.platform == 'android':
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)'
            )
        else:
            self.driver.execute_script('mobile: scroll', {'direction': 'down'})

    def horizontal_scroll(self, direction="right"):
        """Performs a horizontal scroll."""
        if self.platform == 'android':
            cmd = "scrollForward()" if direction == "right" else "scrollBackward()"
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().{cmd}'
            )
        else:
            self.driver.execute_script('mobile: scroll', {'direction': direction})

    def swipe_down(self):
        """A simple generic swipe down (for refreshing or moving the view)."""
        if self.platform == 'android':
            # Fast swipe using UiScrollable
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()')
        else:
            # Native iOS swipe
            self.driver.execute_script('mobile: swipe', {'direction': 'up'})  # 'up' moves view down

    # *******************************************************+
    # **********           LONG PRESS               **********
    # *******************************************************+

    def long_press_element(self, locator, duration):
        """
        Performs a long press on an element.
        :param locator: Tuple (By.XPATH, "query")
        :param duration: Time in seconds
        """
        actions = ActionChains(self.driver)
        pointer = PointerInput(interaction.POINTER_TOUCH, 'touch')
        action_builder = ActionBuilder(self.driver, mouse=pointer)
        LongPress = self.driver.find_element(locator)
        action_builder.pointer_action.move_to(LongPress).pointer_down().pause(duration).pointer_up()
        actions.w3c_actions = action_builder
        actions.perform()

    # *******************************************************+
    # **********           TAP                      **********
    # *******************************************************+
    def tap_element(self, locator):
        """
        Performs a tap on an element.
        :param locator: Tuple (By.XPATH, "query")
        """
        actions = ActionChains(self.driver)
        pointer = PointerInput(interaction.POINTER_TOUCH, 'touch')
        action_builder = ActionBuilder(self.driver, mouse=pointer)
        LongPress = self.driver.find_element(locator)
        action_builder.pointer_action.move_to(LongPress).pointer_down().pause().pointer_up()
        actions.w3c_actions = action_builder
        actions.perform()
