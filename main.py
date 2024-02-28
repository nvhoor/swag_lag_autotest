from enum import Enum

import pytest
from selenium import webdriver

from src import const
from src.login import login
from src.checkout import checkout
from src.shopping_cart import shopping_cart


class SKIP_TEST(Enum):
    STANDARD_USER = False
    LOCKED_OUT_USER = True
    PROBLEM_USER = True
    PERFORMANCE_GLITCH_USER = True
    ERROR_USER = True
    VISUAL_USER = True


@pytest.mark.skipif(SKIP_TEST.STANDARD_USER.value, reason="disable")
def test_standard_user():
    print("standard_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(const.IMPLICITLY_WAIT)
    login.test_login(driver, "standard_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    shopping_cart.test_add_something_from_product_detail_page(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


@pytest.mark.skipif(SKIP_TEST.LOCKED_OUT_USER.value, reason="disable")
def test_locked_out_user():
    # locked_out_user
    print("locked_out_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(const.IMPLICITLY_WAIT)
    login.test_login(driver, "locked_out_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


@pytest.mark.skipif(SKIP_TEST.PROBLEM_USER.value, reason="disable")
def test_problem_user():
    # problem_user
    print("problem_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(const.IMPLICITLY_WAIT)
    login.test_login(driver, "problem_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


@pytest.mark.skipif(SKIP_TEST.PERFORMANCE_GLITCH_USER.value, reason="disable")
def test_performance_glitch_user():
    # performance_glitch_user
    print("performance_glitch_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(const.IMPLICITLY_WAIT)
    login.test_login(driver, "performance_glitch_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


@pytest.mark.skipif(SKIP_TEST.ERROR_USER.value, reason="disable")
def test_error_user():
    # error_user
    print("error_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(const.IMPLICITLY_WAIT)
    login.test_login(driver, "error_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


@pytest.mark.skipif(SKIP_TEST.VISUAL_USER.value, reason="disable")
def test_visual_user():
    # visual_user
    print("visual_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(const.IMPLICITLY_WAIT)
    login.test_login(driver, "visual_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()
