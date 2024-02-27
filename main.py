from selenium import webdriver

from src import const
from src.login import login
from src.checkout import checkout
from src.shopping_cart import shopping_cart


def test_standard_user():
    print("standard_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(3)
    login.test_login(driver, "standard_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


def test_locked_out_user():
    # locked_out_user
    print("locked_out_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(3)
    login.test_login(driver, "locked_out_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


def test_problem_user():
    # problem_user
    print("problem_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(3)
    login.test_login(driver, "problem_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


def test_performance_glitch_user():
    # performance_glitch_user
    print("performance_glitch_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(3)
    login.test_login(driver, "performance_glitch_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


def test_error_user():
    # error_user
    print("error_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(3)
    login.test_login(driver, "error_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()


def test_visual_user():
    # visual_user
    print("visual_user")
    driver = webdriver.Chrome()
    driver.get(const.BASE_URL)
    driver.implicitly_wait(3)
    login.test_login(driver, "visual_user", "secret_sauce")
    shopping_cart.test_add_something_to_cart(driver)
    checkout.test_order_something(driver, "Van Ho", "Nguyen", "550000")
    login.test_logout(driver)
    driver.quit()