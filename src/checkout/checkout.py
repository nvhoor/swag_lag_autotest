from time import sleep

from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By

from src import const


# Test case: sheet 'Checkout' => caseId: 2
def test_order_something(driver: ChromiumDriver, first_name, last_name, postal_code):
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    assert current_url == const.INVENTORY_URL, f"Not on inventory page: current url={current_url}"
    print(current_url)

    try:
        shopping_cart_badge = driver.find_element(By.CLASS_NAME, value="shopping_cart_badge")
        num_selected_products_actual = shopping_cart_badge.text
    except:
        num_selected_products_actual = 0
    cart_icon = driver.find_element(By.ID, value="shopping_cart_container")
    cart_icon.click()
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    assert current_url == const.CART_URL, f"Not on cart page: current url={current_url}"
    print(current_url)
    # TODO: check the cart displays the correct list of selected products(name, image, quantity, price,...) via database or configs
    shopping_cart_badge = driver.find_element(By.CLASS_NAME, value="shopping_cart_badge")
    num_selected_product = shopping_cart_badge.text
    assert num_selected_products_actual == str(
        num_selected_product), "Shopping cart badge show in correct number selected products."
    checkout_btn = driver.find_element(By.ID, value="checkout")
    is_enabled = checkout_btn.is_enabled()
    assert is_enabled, f"Checkout button not enabled."

    checkout_btn.click()
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    assert current_url == const.CHECKOUT_INFO_URL, f"Not show checkout input information page: current url={current_url}"
    print(current_url)
    first_name_field = driver.find_element(By.ID, value="first-name")
    last_name_field = driver.find_element(By.ID, value="last-name")
    postal_code_field = driver.find_element(By.ID, value="postal-code")
    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    postal_code_field.send_keys(postal_code)
    continue_btn = driver.find_element(By.ID, value="continue")
    continue_btn.click()
    sleep(const.TIME_WAIT_AFTER_ACTION)
    # TODO: check Displays the correct list of selected products(name, image, quantity, price,...). Displays correct shipping info, total price, tax and final price.
    current_url = driver.current_url
    assert current_url == const.CHECKOUT_OVERVIEW_URL, f"Not show checkout overview page: current url={current_url}"
    print(current_url)

    finish_btn = driver.find_element(By.ID, value="finish")
    finish_btn.click()
    sleep(const.TIME_WAIT_AFTER_ACTION)
    checkout_complete_container = driver.find_element(By.ID, value="checkout_complete_container")
    current_url = driver.current_url
    is_displayed = checkout_complete_container.is_displayed()
    assert current_url == const.CHECKOUT_FINISH_URL and is_displayed, f"Not show finish page: current url={current_url}, is_displayed={is_displayed}"
    print(current_url)

    back_to_products_btn = driver.find_element(By.ID, value="back-to-products")
    back_to_products_btn.click()
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    assert current_url == const.INVENTORY_URL, f"Not back to inventory page: current url={current_url}"
    print(current_url)
