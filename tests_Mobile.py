import time
from select import select
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.firefox import webdriver

# from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions

import pytest


@pytest.fixture()
def driver():
    # selenium grid
    # driver = webdriver.Remote("http://localhost:4444",desired_capabilities= dc)
    Firefox_driver_binary = "./geckodriver"
    fire_fox_options = FireFoxOptions()
    fire_fox_options.add_argument("--width=414")
    fire_fox_options.add_argument("--height=896")
    fire_fox_options.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS "
                                                                  "X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                                                                  "Version/14.0.3 Mobile/15E148 Safari/604.1")
    ser_firefox = FirefoxService(Firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox, options=fire_fox_options)
    yield driver
    driver.close()



# Positive Scenario
def test_registration(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR,"ul.wt-display-flex-xs > li:nth-child(1) > a:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR," #join_neu_email_field").click()
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("pepsi1@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"button.wt-btn:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("Amar")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(5)
    msg = driver.find_element(By.CSS_SELECTOR, ".wt-p-md-3")
    txt = msg.text
    assert "Welcome to Etsy, Amar!" == txt


#Negative Scenario
def test_Invalid_Email(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR,"ul.wt-display-flex-xs > li:nth-child(1) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amar09090@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn:nth-child(1)").click()
    time.sleep(3)
    msg = driver.find_element(By.CSS_SELECTOR,"div.wt-grid:nth-child(9) > div:nth-child(1) > div:nth-child(1)").text
    assert "Create your account\nRegistration is easy." == msg



def test_mandatory_message(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR,"ul.wt-display-flex-xs > li:nth-child(1) > a:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, " #join_neu_email_field").click()
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("besle@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(5)
    err_message = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_first_name_field-error")
    err_text = err_message.text
    assert "First name can't be blank." == err_text



def test_incorect_values(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR, "ul.wt-display-flex-xs > li:nth-child(1) > a:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, " #join_neu_email_field").click()
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("3234234234324")
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn:nth-child(1)").click()
    time.sleep(2)
    invalidContent = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_email_field-error")
    txt = invalidContent.text
    assert "Please enter a valid email address." == txt
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("hala@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("123123131")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("asdasdasdad")
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(2)
    invalidUsername = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_first_name_field-error")
    txt1 = invalidUsername.text
    assert "Your first name contains invalid characters." == txt1


def test_search_product(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR, "ul.wt-display-flex-xs > li:nth-child(1) > a:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, " #join_neu_email_field").click()
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amaro4@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678(")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, " button.wt-btn:nth-child(1)").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR,"li.shopping-window:nth-child(1) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR,"li.wt-order-xs-0:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
    driver.get("https://www.etsy.com/il-en/listing/1112269751/set-of-14-boho-wall-decorseagrass?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=wall+decor&ref=sc_gallery-1-1&pro=1&plkey=a2c1840978be685031e5b9d4b8b1cb4750917305%3A1112269751")
    name = driver.find_element(By.CSS_SELECTOR,"h1.wt-text-caption").text
    driver.find_element(By.CSS_SELECTOR,"#global-enhancements-search-query").send_keys(name)
    driver.find_element(By.CSS_SELECTOR,".wt-input-btn-group__btn").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"li.wt-order-xs-0:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
    driver.get("https://www.etsy.com/il-en/listing/1112269751/set-of-14-boho-wall-decorseagrass?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=Set+of+14+Boho+Wall+Decor%2CSeagrass+Baskets+Wall+Decor%2C+Wicker+Hanging+Wall+Basket%2C+Natural+Boho+Wall+Decor-Boho+Decor%2C+Father%26%2339%3Bs+Day+Gift&ref=sc_gallery-1-1&pro=1&plkey=813ee05c4d383b15cda03223601b5a22f6cbc82e%3A1112269751")
    time.sleep(2)
    txt = driver.find_element(By.CSS_SELECTOR,"h1.wt-text-caption").text
    assert txt == name
    time.sleep(2)


def test_buy_product(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR, "li.shopping-window:nth-child(6) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "li.wt-order-xs-0:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
    driver.get("https://www.etsy.com/il-en/listing/823311406/diy-solar-printing-kit-craft-kit?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=craft+kits&ref=sc_gallery-1-1&frs=1&etp=1&plkey=026c479119a2a50d7b8a25a9fcaef8070cebddda%3A823311406")
    time.sleep(3)
    driver.find_element(By.ID, "variation-selector-0").click()
    dropdown = driver.find_element(By.ID, "variation-selector-0")
    dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-0 > option:nth-child(4)").click()
    time.sleep(3)
    # driver.find_element(By.ID, "variation-selector-1").click()
    # dropdown = driver.find_element(By.ID, "variation-selector-1")
    # dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-1 > option:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR,"div.wt-width-full:nth-child(7) > button:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "ul.wt-display-flex-xs > li:nth-child(1) > a:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, " #join_neu_email_field").click()
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("barake.amaro@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("123456&*")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, " button.wt-btn:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element")
    dropdown.find_element(By.CSS_SELECTOR, "#multi-shop-cart-list > div > div > div.wt-grid.wt-position-relative.wt-pl-xs-0.wt-pr-xs-0 > ul > li > ul > li > div > div.wt-flex-xs-3.wt-pl-xs-2.wt-pl-lg-3 > div > div.wt-grid__item-xs-5.wt-hide-xs.wt-show-lg.wt-pl-xs-3 > div > div.wt-grid__item-xs-5.wt-pb-xs-1.wt-pr-xs-0 > div > div > div > select > option:nth-child(2)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"button.proceed-to-checkout:nth-child(1) > span:nth-child(1)").click()
    driver.find_element(By.ID, "country_id9-select").click()
    driver.find_element(By.ID,"name10-input").click()
    driver.find_element(By.ID, "name10-input").send_keys("Amar Barake")
    driver.find_element(By.ID, "first_line11-input").send_keys("Burj-Sukar, Elain")
    driver.find_element(By.ID, "second_line12-input").send_keys("6")
    driver.find_element(By.ID, "city13-input").send_keys("Shefa-amr")
    driver.find_element(By.ID, "zip14-input").send_keys("2020000")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#shipping-address-form > div.wt-pl-xs-2.wt-pr-xs-2.wt-pl-md-0.wt-pr-md-0.wt-mt-xs-2 > button").click()
    time.sleep(2)


def test_add_to_whishlist(driver):
    driver.get('https://www.etsy.com/')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "li.shopping-window:nth-child(6) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "li.wt-order-xs-0:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
    driver.get("https://www.etsy.com/il-en/listing/823311406/diy-solar-printing-kit-craft-kit?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=craft+kits&ref=sc_gallery-1-1&frs=1&etp=1&plkey=026c479119a2a50d7b8a25a9fcaef8070cebddda%3A823311406")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"button.inline-overlay-trigger:nth-child(4)").click()
    time.sleep(4)
    msg = driver.find_element(By.CSS_SELECTOR,"div.wt-grid:nth-child(8) > div:nth-child(1) > div:nth-child(1)").text
    time.sleep(3)
    assert "Before you can do that...\nSign in or register with your email address" == msg



def test_total_price_change(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "li.shopping-window:nth-child(6) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "li.wt-order-xs-0:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
    driver.get( "https://www.etsy.com/il-en/listing/823311406/diy-solar-printing-kit-craft-kit?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=craft+kits&ref=sc_gallery-1-1&frs=1&etp=1&plkey=026c479119a2a50d7b8a25a9fcaef8070cebddda%3A823311406")
    time.sleep(3)
    driver.find_element(By.ID, "variation-selector-0").click()
    dropdown = driver.find_element(By.ID, "variation-selector-0")
    dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-0 > option:nth-child(4)").click()
    time.sleep(3)
    # driver.find_element(By.ID, "variation-selector-1").click()
    # dropdown = driver.find_element(By.ID, "variation-selector-1")
    # dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-1 > option:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, "div.wt-width-full:nth-child(7) > button:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "ul.wt-display-flex-xs > li:nth-child(1) > a:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, " #join_neu_email_field").click()
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("barake.amaro@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("123456&*")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, " button.wt-btn:nth-child(1)").click()
    time.sleep(3)
    curent_price = driver.find_element(By.CSS_SELECTOR,"tbody.wt-text-left-xs > tr:nth-child(5) > td:nth-child(2) > h1:nth-child(1)").text
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element")
    dropdown.find_element(By.CSS_SELECTOR,"#multi-shop-cart-list > div > div > div.wt-grid.wt-position-relative.wt-pl-xs-0.wt-pr-xs-0 > ul > li > ul > li > div > div.wt-flex-xs-3.wt-pl-xs-2.wt-pl-lg-3 > div > div.wt-grid__item-xs-5.wt-hide-xs.wt-show-lg.wt-pl-xs-3 > div > div.wt-grid__item-xs-5.wt-pb-xs-1.wt-pr-xs-0 > div > div > div > select > option:nth-child(2)").click()
    time.sleep(5)
    changed_price = driver.find_element(By.CSS_SELECTOR,"tbody.wt-text-left-xs > tr:nth-child(5) > td:nth-child(2) > h1:nth-child(1)").text
    assert changed_price != curent_price
