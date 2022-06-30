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
    fire_fox_options.add_argument("--width=834")
    fire_fox_options.add_argument("--height=1194")
    fire_fox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) "
                                                                  "AppleWebKit/605.1.15 "
                                                                  "(KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1")
    ser_firefox = FirefoxService(Firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox, options=fire_fox_options)
    yield driver
    driver.close()



# Positive Scenario
def test_registration(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR,  "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn--secondary:nth-child(2)").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("Amar10baer@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("Amar")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(5)
    msg = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(1) > div")
    txt = msg.text
    assert "Welcome to Etsy, Amar!" == txt


# #Negative Scenario
def test_Invalid_Email(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("Ama@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    time.sleep(2)
    invalid_message = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_email_field-error")
    err_invalid = invalid_message.text
    assert "Email address is invalid." == err_invalid



def test_mandatory_message(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"button.wt-btn--secondary:nth-child(2)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amar.ba@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(5)
    err_message = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_first_name_field-error")
    err_text = err_message.text
    assert "First name can't be blank." == err_text



def test_incorect_values(driver):
    driver.get('https://www.etsy.com/')
    driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button.wt-btn--secondary:nth-child(2)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("121143424")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("2312")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("basdasd")
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(6)
    invalidContent = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_email_field-error")
    txt = invalidContent.text
    assert "Please enter a valid email address." == txt
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").clear()
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("vsds@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("2312")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("basdasd")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(4)
    invalidUsername = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_first_name_field-error")
    txt1 = invalidUsername.text
    assert "Your first name contains invalid characters." == txt1


def test_search_product(driver):
    driver.get('https://www.etsy.com/')
    # driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("mrfotaa@gmail.com")
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("834500=")
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,  "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    # time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "li.shopping-window:nth-child(6) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".tab-reorder-container > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
    driver.get( "https://www.etsy.com/il-en/listing/848136290/botanical-linocut-kit-uk-made-includes?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=craft+kits&ref=sc_gallery-1-1&sts=1&plkey=507574a2ac4d9a578d96b8772d5f92c6fbe46fe8%3A848136290")
    name = driver.find_element(By.CSS_SELECTOR, "h1.wt-text-body-03").text
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#global-enhancements-search-query").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, ".global-enhancements-search-input-btn-group__btn").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "li.wt-block-grid__item:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
    driver.get("https://www.etsy.com/il-en/listing/848136290/botanical-linocut-kit-uk-made-includes?click_key=db2460b1454c7fc253a873d440043351e628750b%3A848136290&click_sum=4e4b4fce&ref=search_recently_viewed-1&sts=1")
    time.sleep(2)
    txt = driver.find_element(By.CSS_SELECTOR, "h1.wt-text-body-03").text
    assert txt == name



def test_buy_product(driver):
    driver.get('https://www.etsy.com/')
    time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("mrfotaa@gmail.com")
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("834500=")
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    # time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "li.shopping-window:nth-child(6) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "li.wt-order-xs-2:nth-child(3)").click()
    driver.get("https://www.etsy.com/il-en/listing/1064068324/fancy-sushi-needle-felting-kits-beginner?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=craft+kits&ref=sc_gallery-1-3&bes=1&plkey=a905bff47e9b874a72ef607c5dbe48621e436f7a%3A1064068324")
    time.sleep(4)
    driver.find_element(By.ID, "variation-selector-0").click()
    dropdown = driver.find_element(By.ID, "variation-selector-0")
    dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-0 > option:nth-child(3)").click()
    time.sleep(3)
    # driver.find_element(By.ID, "variation-selector-1").click()
    # dropdown = driver.find_element(By.ID, "variation-selector-1")
    # dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-1 > option:nth-child(3)").click()
    # driver.find_element(By.CSS_SELECTOR, "div.wt-width-full:nth-child(7) > button:nth-child(1)").click()
    # time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "div.wt-width-full:nth-child(7) > button:nth-child(1)").click()
    time.sleep(2)
    # driver.find_element(By.ID, "variation-selector-1").click()
    # dropdown = driver.find_element(By.ID, "variation-selector-1")
    # dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-1 > option:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR,".wt-tooltip--bottom-left > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element")
    dropdown.find_element(By.CSS_SELECTOR, "#multi-shop-cart-list > div > div > div.wt-grid.wt-position-relative.wt-pl-xs-0.wt-pr-xs-0 > ul > li > ul > li > div > div.wt-flex-xs-3.wt-pl-xs-2.wt-pl-lg-3 > div > div.wt-grid__item-xs-5.wt-hide-xs.wt-show-lg.wt-pl-xs-3 > div > div.wt-grid__item-xs-5.wt-pb-xs-1.wt-pr-xs-0 > div > div > div > select > option:nth-child(2)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#multi-shop-cart-list > div > div > div.wt-grid.wt-position-relative.wt-pl-xs-0.wt-pr-xs-0 > div > div > div > form > div:nth-child(6) > div.wt-pb-xs-2 > button").click()
    time.sleep(2)
    driver.find_element(By.ID, "country_id16-select").click()
    driver.find_element(By.ID,"name17-input").click()
    driver.find_element(By.ID, "name17-input").send_keys("Amar Barake")
    driver.find_element(By.ID, "first_line18-input").send_keys("Burj-Sukar, Elain")
    driver.find_element(By.ID, "second_line19-input").send_keys("6")
    driver.find_element(By.ID, "city20-input").send_keys("Shefa-amr")
    driver.find_element(By.ID, "zip21-input").send_keys("2020000")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#shipping-address-form > div.wt-pl-xs-2.wt-pr-xs-2.wt-pl-md-0.wt-pr-md-0.wt-mt-xs-2 > button").click()



def test_add_to_whishlist(driver):
    driver.get('https://www.etsy.com/')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "li.shopping-window:nth-child(6) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".tab-reorder-container > li:nth-child(1)").click()
    driver.get("https://www.etsy.com/il-en/listing/823311406/diy-solar-printing-kit-craft-kit?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=craft+kits&ref=sc_gallery-1-1&pro=1&frs=1&plkey=5844e2f4f9bc134dc2d362f453e75761172b86d3%3A823311406")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "a.wt-btn--transparent:nth-child(2)").click()
    time.sleep(4)
    msg = driver.find_element(By.CSS_SELECTOR, "div.wt-grid:nth-child(8) > div:nth-child(1) > div:nth-child(1)").text
    time.sleep(3)
    assert "Before you can do that...\nSign in or register with your email address" == msg


def test_total_price_change(driver):
    driver.get('https://www.etsy.com/')
    time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("mrfotaa@gmail.com")
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("834500=")
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    # time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "li.shopping-window:nth-child(6) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "li.wt-order-xs-2:nth-child(3)").click()
    driver.get("https://www.etsy.com/il-en/listing/1064068324/fancy-sushi-needle-felting-kits-beginner?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=craft+kits&ref=sc_gallery-1-3&bes=1&plkey=a905bff47e9b874a72ef607c5dbe48621e436f7a%3A1064068324")
    time.sleep(3)
    driver.find_element(By.ID, "variation-selector-0").click()
    dropdown = driver.find_element(By.ID, "variation-selector-0")
    dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-0 > option:nth-child(3)").click()
    time.sleep(3)
    # driver.find_element(By.ID, "variation-selector-1").click()
    # dropdown = driver.find_element(By.ID, "variation-selector-1")
    # dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-1 > option:nth-child(3)").click()
    # driver.find_element(By.CSS_SELECTOR, "div.wt-width-full:nth-child(7) > button:nth-child(1)").click()
    # time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "div.wt-width-full:nth-child(7) > button:nth-child(1)").click()
    time.sleep(2)
    # driver.find_element(By.ID, "variation-selector-1").click()
    # dropdown = driver.find_element(By.ID, "variation-selector-1")
    # dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-1 > option:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, ".wt-tooltip--bottom-left > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element")
    dropdown.find_element(By.CSS_SELECTOR,"#multi-shop-cart-list > div > div > div.wt-grid.wt-position-relative.wt-pl-xs-0.wt-pr-xs-0 > ul > li > ul > li > div > div.wt-flex-xs-3.wt-pl-xs-2.wt-pl-lg-3 > div > div.wt-grid__item-xs-5.wt-hide-xs.wt-show-lg.wt-pl-xs-3 > div > div.wt-grid__item-xs-5.wt-pb-xs-1.wt-pr-xs-0 > div > div > div > select > option:nth-child(2)").click()
    time.sleep(3)
    curent_price = driver.find_element(By.CSS_SELECTOR,".wt-no-wrap > .wt-text-title-01").text
    driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element")
    dropdown.find_element(By.CSS_SELECTOR,"#multi-shop-cart-list > div > div > div.wt-grid.wt-position-relative.wt-pl-xs-0.wt-pr-xs-0 > ul > li > ul > li > div > div.wt-flex-xs-3.wt-pl-xs-2.wt-pl-lg-3 > div > div.wt-grid__item-xs-5.wt-hide-xs.wt-show-lg.wt-pl-xs-3 > div > div.wt-grid__item-xs-5.wt-pb-xs-1.wt-pr-xs-0 > div > div > div > select > option:nth-child(2)").click()
    time.sleep(5)
    changed_price = driver.find_element(By.CSS_SELECTOR,".wt-no-wrap > .wt-text-title-01").text
    assert changed_price != curent_price
