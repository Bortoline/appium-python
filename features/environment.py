# Hooks file
from os.path import join

# Appium and webdriver
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Page Objects
from features.support.pages.android.add_page_objects_to_android_context import add_page_objects_to_android_context

# Constants
from features.support import constants


def before_all(context):
    global userdata  # Get user data from behave start command
    global desired_caps
    global host_appium_address  # Location of test run

    userdata = context.config.userdata
    context.config_0 = userdata.get('config_0', 'False')

    desired_caps = {}
    host_appium_address = 'http://localhost:4723/wd/hub'

    # ANDROID
    if userdata["platform"] == "Android" and userdata["location"] != "devicefarm":
        add_page_objects_to_android_context(context)

        desired_caps['platformName'] = userdata["platform"]
        desired_caps['deviceName'] = userdata["platform"]
        desired_caps['app'] = join(constants.PATH, 'application', 'android', userdata["app_name"])
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['autoGrantPermissions'] = 'true'
        desired_caps['newCommandTimeout'] = '0'
        desired_caps['appWaitActivity'] = '*.OnboardingActivity'

        if userdata["location"] == "saucelabs":  # To Run tests in saucelabs
            desired_caps['appiumVersion'] = "1.9.1"
            desired_caps['application'] = "sauce-storage:" + userdata["app_name"]
            desired_caps['platformVersion'] = "7.1.1"

            host_appium_address = 'http://bortoline:6e029cc9-3540' \
                                  '-4872-9906-7cfe055abaf6@ondemand.saucelabs.com:80/wd/hub'

    # IOS
    if userdata["platform"] == "IOS" and userdata["location"] != "devicefarm":
        add_page_objects_to_android_context(context)  # Change to IOS Context

        desired_caps['application'] = join(constants.PATH, 'application', 'ios', userdata["app_name"])

        if userdata["location"] == "saucelabs":  # To Run tests in saucelabs
            desired_caps['appiumVersion'] = "1.9.1"
            desired_caps['application'] = "sauce-storage:" + userdata["app_name"]

            host_appium_address = 'http://bortoline:6e029cc9-3540-4872-' \
                                  '9906-7cfe055abaf6@ondemand.saucelabs.com:80/wd/hub'


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    global driver
    driver = webdriver.Remote(host_appium_address, desired_caps)
    driver.implicitly_wait(10)

    context.driver = driver
    # context.wait = WebDriverWait(driver, 10)
    context.By = By
    context.EC = EC


def before_tag(context, tag):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_tag(context, step):
    pass


def after_scenario(context, scenario):

    if scenario.status == "failed":
        import re
        from time import gmtime, strftime

        scenario_name = re.sub('[^a-z A-Z0-9\n]', '', scenario.name)
        file_name = "SS_{0}_{1}.png".format(scenario_name.replace(" ", "_"), strftime("%Y-%m-%d_%H:%M:%S", gmtime()))

        driver.save_screenshot(join(constants.PATH, "screenshot", file_name))


def after_feature(context, feature):
    pass
    # driver.remove_app('hands.android.webmotors')  # Remove app after feature test


def after_all(context):
    driver.quit()
