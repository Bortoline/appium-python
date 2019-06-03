from selenium.common.exceptions import NoSuchElementException


class BaseScreen(object):
    def __init__(self, context):
        self.context = context

    def get_element(self, locator_method, locator_value):
        """
        Returns element based on provided locators.

        locator_method and locator_value.
        :param locator_method:
        :param locator_value: str or list
        :return:
        """

        if type(locator_value) is str:
            return self.get_element_by_type(locator_method, locator_value)
        elif type(locator_value) is list:
            for value in locator_value:
                try:
                    return self.get_element_by_type(locator_method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_elements(self, locator_method, locator_value):
        """
        Returns elements based on provided locators.

        locator_method and locator_value.
        :param locator_method:
        :param locator_value: str or list
        :return:
        """

        if type(locator_value) is str:
            return self.get_elements_by_type(locator_method, locator_value)
        elif type(locator_value) is list:
            for value in locator_value:
                try:
                    return self.get_elements_by_type(locator_method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_element_by_type(self, locator_method, locator_value):
        if locator_method == 'accessibility_id':
            return self.context.driver.find_element_by_accessibility_id(locator_value)
        elif locator_method == 'ios':
            return self.context.driver.find_element_by_ios_uiautomation(locator_value)
        elif locator_method == 'class_name':
            return self.context.driver.find_element_by_class_name(locator_value)
        elif locator_method == 'id':
            return self.context.driver.find_element_by_id(locator_value)
        elif locator_method == 'xpath':
            return self.context.driver.find_element_by_xpath(locator_value)
        elif locator_method == 'name':
            return self.context.driver.find_element_by_name(locator_value)
        else:
            raise AssertionError('Invalid locator method.')

    def get_elements_by_type(self, locator_method, locator_value):
        if locator_method == 'accessibility_id':
            return self.context.driver.find_elements_by_accessibility_id(locator_value)
        elif locator_method == 'ios':
            return self.context.driver.find_elements_by_ios_uiautomation(locator_value)
        elif locator_method == 'class_name':
            return self.context.driver.find_elements_by_class_name(locator_value)
        elif locator_method == 'id':
            return self.context.driver.find_elements_by_id(locator_value)
        elif locator_method == 'xpath':
            return self.context.driver.find_elements_by_xpath(locator_value)
        elif locator_method == 'name':
            return self.context.driver.find_elements_by_name(locator_value)
        else:
            raise AssertionError('Invalid locator method.')

    # element visible
    def is_visible(self, locator_method, locator_value):
        try:
            return self.get_element(locator_method, locator_value).is_displayed()
        except NoSuchElementException:
            return False

    # element present
    def is_present(self, locator_method, locator_value):
        try:
            self.get_element(locator_method, locator_value)
            return True
        except NoSuchElementException:
            return False

    # waits
    def wait_visible(self, locator_method, locator_value, timeout=10):
        from time import sleep
        i = 0
        while i != timeout:
            try:
                self.is_visible(locator_method, locator_value)
                return self.get_element(locator_method, locator_value)
            except NoSuchElementException:
                sleep(1)
                i += 1
        raise AssertionError('Element never became visible: %s (%s)' % (locator_method, locator_value))

    def wait_for_text(self, locator_method, locator_value, text, timeout=10):
        i = 0
        while i != timeout:
            try:
                element = self.get_element(locator_method, locator_value)
                element_text = element.text
                if element_text.lower() == text.lower():
                    return True
                else:
                    pass
            except NoSuchElementException:
                pass
            from time import sleep
            sleep(1)
            i += 1
        raise AssertionError('Element text never became visible: %s (%s) - %s' % (locator_method, locator_value, text))

    def tap_element_find_by_text(self, locator_method, locator_value, tap_text):
        self.wait_visible(locator_method, locator_value)
        element_list = self.get_elements(locator_method, locator_value)
        for element in element_list:
            if element.text == tap_text:
                return element.click()

    # tap or click element
    def tap_button(self, locator_method, locator_value):
        element = self.wait_visible(locator_method, locator_value)
        element.click()

    # send keys
    def send_keys(self, locator_method, locator_value, text):
        element = self.wait_visible(locator_method, locator_value)
        element.send_keys(text)

    # get text
    def get_element_text(self, locator_method, locator_value):
        element = self.wait_visible(locator_method, locator_value)
        return element.text

    # get checked status
    def get_element_checked_status(self, locator_method, locator_value):
        element = self.wait_visible(locator_method, locator_value)
        return eval(element.get_attribute('checked').capitalize())

    # clear element
    def clear_element(self, locator_method, locator_value):
        element = self.wait_visible(locator_method, locator_value)
        element.clear()

    # get element enabled status
    def get_element_enabled_status(self, locator_method, locator_value):
        try:
            element = self.wait_visible(locator_method, locator_value)
            return element.is_enabled()
        except NoSuchElementException:
            return False

    # Scroll screen using elements
    def scroll_from_element_to_element(self, id_from_element, id_element_destination):
        from appium.webdriver.common.touch_action import TouchAction
        actions = TouchAction(self.context.driver)

        from_element = self.context.driver.find_element_by_id(id_from_element)
        destination_element = self.context.driver.find_element_by_id(id_element_destination)

        from_element_location = from_element.location
        destination_element_location = destination_element.location

        actions.press(
            x=from_element_location['x'] - 2,
            y=from_element_location['y'] - 2) \
            .move_to(
            x=destination_element_location['x'],
            y=destination_element_location['y']) \
            .release().perform()

    # Insert Android Keys -> Number
    def insert_text_android_keys_id(self, _id, text):
        field = self.context.driver.find_element_by_id(_id)
        field.clear()
        field.click()
        char_list = self.android_keys_number(text)
        for char in char_list:
            self.context.driver.press_keycode(char)

    def insert_text_android_keys_class(self, _class, text):
        field = self.context.driver.find_element_by_class_name(_class)
        field.clear()
        field.click()
        char_list = self.android_keys_number(text)
        for char in char_list:
            self.context.driver.press_keycode(char)

    @staticmethod
    def android_keys_number(text):
        android_keys_dict = {
            "0": 7,
            "1": 8,
            "2": 9,
            "3": 10,
            "4": 11,
            "5": 12,
            "6": 13,
            "7": 14,
            "8": 15,
            "9": 16,
            "*": 17,
            "#": 18,
            ",": 55,
            ".": 56,
            "`": 68,
            "-": 69,
            "=": 70,
            "[": 71,
            "]": 72,
            "\\": 73,
            ";": 74,
            "'": 75,
            "/": 76,
            "@": 77,
            "+": 81,
            "a": 29,
            "b": 30,
            "c": 31,
            "d": 32,
            "e": 33,
            "f": 34,
            "g": 35,
            "h": 36,
            "i": 37,
            "j": 38,
            "k": 39,
            "l": 40,
            "m": 41,
            "n": 42,
            "o": 43,
            "p": 44,
            "q": 45,
            "r": 46,
            "s": 47,
            "t": 48,
            "u": 49,
            "v": 50,
            "x": 51,
            "y": 52,
            "z": 53,
            "del": 67
        }
        mapped_string = []
        for char in text:
            try:
                mapped_string.append(android_keys_dict[char])
            except KeyError:
                pass

        return mapped_string

    # Generic webdriver functions
    def base_ensure_visible_by_id(self, _id):
        self.context.wait.until(self.context.EC.presence_of_element_located((self.context.By.ID, _id)))

    def base_ensure_visible_by_xpath(self, _xpath):
        self.context.wait.until(self.context.EC.presence_of_element_located((self.context.By.XPATH, _xpath)))

    def base_ensure_visible_by_class(self, _class):
        self.context.wait.until(self.context.EC.presence_of_element_located((self.context.By.CLASS, _class)))

    def base_ensure_until_not_visible_by_id(self, _id):
        self.context.wait.until_not(self.context.EC.presence_of_element_located((self.context.By.ID, _id)))

    def wait_not_invisibility_of_element_by_id(self, _id):
        self.context.wait.until_not(self.context.EC.invisibility_of_element((self.context.By.ID, _id)))

    def wait_invisibility_of_element_by_id(self, _id):
        self.context.wait.until(self.context.EC.invisibility_of_element((self.context.By.ID, _id)))

    def wait_text_to_be_present_in_element_by_id(self, _id, date):
        self.context.wait.until(self.context.EC.text_to_be_present_in_element((self.context.By.ID, _id), date))