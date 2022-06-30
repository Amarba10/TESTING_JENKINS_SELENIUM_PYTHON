import time
from select import select
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pytest


@pytest.fixture()
def driver():

    Firefox_driver_binary = "./geckodriver"
    ser_firefox = FirefoxService(Firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox)


    yield driver
    driver.close()


# Positive Scenario
def test_registration(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,  "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(1) > div > button").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amar10ba@gmail.com")
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
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amar@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    time.sleep(2)
    invalid_message = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_password_field-error")
    err_invalid = invalid_message.text
    assert "Password was incorrect" == err_invalid



def test_mandatory_message(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(1) > div > button").click()
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
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(1) > div > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("121143424")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("2312")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("basdasd")
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(4)
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
    driver.maximize_window()
    # driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("toti@hotmail.com")
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678*")
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,  "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    # time.sleep(4)
    element = driver.find_element(By.ID, "catnav-primary-link-10923")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(4)
    driver.find_element(By.ID, "catnav-l4-10927").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".wt-block-grid__item:nth-child(1) .ingress-title").click()
    driver.get("https://www.etsy.com/il-en/listing/1226189086/here-comes-the-sun-t-shirt-for-women?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-1&pro=1&plkey=c08a7e0357c01f8d92b0edc780088529da8ffb2a%3A1226189086")
    name = driver.find_element(By.CSS_SELECTOR,"#listing-page-cart > div.wt-mb-xs-2 > h1")
    txt = name.text
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#global-enhancements-search-query").send_keys(txt)
    driver.find_element(By.CSS_SELECTOR, "#gnav-search > div > div.wt-input-btn-group.global-enhancements-search-input-btn-group.wt-menu__trigger.emphasized_search_bar.emphasized_search_bar_grey_bg > button").click()
    driver.get("https://www.etsy.com/il-en/listing/1226189086/here-comes-the-sun-t-shirt-for-women?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=Here+Comes+the+Sun+T+Shirt+For+Women%2C+Travel+Beach+Vacation+Shirt%2C+Sunshine+Shirt%2C+Beatles+Retro+Shirt%2C+Motivational+Shirt%2C+Gift+for+Her&ref=sc_gallery-1-1&pro=1&plkey=850212bf1523a8796d875b681954ef5ed07aac77%3A1226189086")
    time.sleep(3)
    tshirt = driver.find_element(By.CSS_SELECTOR, "#listing-page-cart > div.wt-mb-xs-2 > h1")
    result = tshirt.text
    assert result == txt


def test_buy_product(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amarbarake19@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    time.sleep(2)
    element = driver.find_element(By.ID, "catnav-primary-link-10923")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    driver.find_element(By.ID, "catnav-l4-10926").click()
    time.sleep(2)
    # driver.get("https://www.etsy.com/il-en/listing/1186609384/women-summer-cotton-dresses-nine-point?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-2&pro=1&frs=1&plkey=a295f42576f834c6f7f0a0d21fc2c98d280aaf3f%3A1186609384")
    driver.get("https://www.etsy.com/il-en/listing/1095947005/bestseller-gipsy-layered-boho-skirt-maxi?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-4&frs=1&plkey=2c20db55b80a7061cfcf6ebf11ea1788473e185d%3A1095947005")
    time.sleep(3)
    driver.find_element(By.ID, "variation-selector-0").click()
    dropdown = driver.find_element(By.ID, "variation-selector-0")
    dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-0 > option:nth-child(4)").click()
    time.sleep(3)
    # driver.find_element(By.ID, "variation-selector-1").click()
    # dropdown = driver.find_element(By.ID, "variation-selector-1")
    # dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-1 > option:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR,"#listing-page-cart > div.wt-mb-xs-6.wt-mb-lg-0 > div:nth-child(1) > div.wt-display-flex-xs.wt-flex-direction-column-xs.wt-flex-wrap.wt-flex-direction-row-md.wt-flex-direction-column-lg > div > form > div > button").click()
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
    driver.maximize_window()
    time.sleep(2)
    element = driver.find_element(By.ID, "catnav-primary-link-10923")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    driver.find_element(By.ID, "catnav-l4-10926").click()
    time.sleep(2)
    driver.get("https://www.etsy.com/il-en/listing/1095947005/bestseller-gipsy-layered-boho-skirt-maxi?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-4&frs=1&plkey=2c20db55b80a7061cfcf6ebf11ea1788473e185d%3A1095947005")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#listing-right-column > div > div.body-wrap.wt-body-max-width.wt-display-flex-md.wt-flex-direction-column-xs > div.image-col.wt-order-xs-1.wt-mb-lg-6 > div > div > div > button").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(2) > span > a").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR,"#content > div > div.wt-body-max-width > div > div.wt-mt-xs-3.wt-mb-xs-1.wt-mt-md-5.wt-mb-md-2 > div > a.wt-btn.wt-btn--tertiary.wt-btn--icon.wt-ml-xs-3.inline-overlay-trigger.guest-favorites-edit-action").click()
    time.sleep(3)
    msg = driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div.wt-mb-xs-3").text
    time.sleep(3)
    assert "Before you can do that...\nSign in or register with your email address" == msg



def test_total_price_change(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amarbarake19@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    time.sleep(2)
    element = driver.find_element(By.ID, "catnav-primary-link-10923")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    driver.find_element(By.ID, "catnav-l4-10926").click()
    time.sleep(2)
    # driver.get("https://www.etsy.com/il-en/listing/1186609384/women-summer-cotton-dresses-nine-point?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-2&pro=1&frs=1&plkey=a295f42576f834c6f7f0a0d21fc2c98d280aaf3f%3A1186609384")
    driver.get( "https://www.etsy.com/il-en/listing/1095947005/bestseller-gipsy-layered-boho-skirt-maxi?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-4&frs=1&plkey=2c20db55b80a7061cfcf6ebf11ea1788473e185d%3A1095947005")
    time.sleep(3)
    driver.find_element(By.ID, "variation-selector-0").click()
    dropdown = driver.find_element(By.ID, "variation-selector-0")
    dropdown.find_element(By.CSS_SELECTOR, "#variation-selector-0 > option:nth-child(4)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#listing-page-cart > div.wt-mb-xs-6.wt-mb-lg-0 > div:nth-child(1) > div.wt-display-flex-xs.wt-flex-direction-column-xs.wt-flex-wrap.wt-flex-direction-row-md.wt-flex-direction-column-lg > div > form > div > button").click()
    curent_price = driver.find_element(By.CSS_SELECTOR,".wt-no-wrap > .wt-text-title-01").text
    driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-5 > .wt-grid .wt-select__element")
    dropdown.find_element(By.CSS_SELECTOR,"#multi-shop-cart-list > div > div > div.wt-grid.wt-position-relative.wt-pl-xs-0.wt-pr-xs-0 > ul > li > ul > li > div > div.wt-flex-xs-3.wt-pl-xs-2.wt-pl-lg-3 > div > div.wt-grid__item-xs-5.wt-hide-xs.wt-show-lg.wt-pl-xs-3 > div > div.wt-grid__item-xs-5.wt-pb-xs-1.wt-pr-xs-0 > div > div > div > select > option:nth-child(2)").click()
    time.sleep(5)
    changed_price = driver.find_element(By.CSS_SELECTOR,".wt-no-wrap > .wt-text-title-01").text
    assert changed_price != curent_price
