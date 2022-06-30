import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver as webdriver
# from appium import webdriver as appium_webdriver
from appium import webdriver

@pytest.fixture()
def driver():
    dc = {
        'platformName': 'Android',
        'platformVersion': ' 8.1',
        'deviceName': 'Pixel 2 API 27',
        'automationName': 'Appium',
        'browserName': 'chrome'
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=dc)
    yield driver
    driver.close()

# @pytest.fixture(autouse=True)
# def driver():
#     dc = {
#         'platformName': 'ios',
#         'platformVersion': ' 15.4',
#         'deviceName': 'ipohne SE',
#         'automationName': 'XCUITest',
#         'browserName': 'Safari'
#     }
#     driver = appium_webdriver.Remote("http://192.168.1.189:4444", desired_capabilities=dc)
#     yield driver
#     driver.close()


def test_google(driver):
    driver.get("https://www.google.com/webhp?hl=iw&sa=X&ved=0ahUKEwiaoaiVic74AhUogv0HHal2An8QPAgI")
    time.sleep(5)