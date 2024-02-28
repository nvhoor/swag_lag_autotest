from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src import const


# Test case: sheet 'Checkout' => caseId: 2
def test_order_something(driver: ChromiumDriver, first_name, last_name, postal_code):
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    assert current_url == const.INVENTORY_URL, f"Not on inventory page: current url={current_url}"
    print(current_url)
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "inventory_container")))

    try:
        shopping_cart_badge = driver.find_element(By.CLASS_NAME, value="shopping_cart_badge")
        num_selected_products_actual = shopping_cart_badge.text
    except NoSuchElementException:
        num_selected_products_actual = 0
    cart_icon = driver.find_element(By.ID, value="shopping_cart_container")
    cart_icon.click()
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "cart_contents_container")))
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
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "checkout_info_container")))
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
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "checkout_summary_container")))
    sleep(const.TIME_WAIT_AFTER_ACTION)
    # TODO: check displays the correct list of selected products(name, image, quantity, price,...). Displays correct shipping info, total price, tax and final price.
    current_url = driver.current_url
    assert current_url == const.CHECKOUT_OVERVIEW_URL, f"Not show checkout overview page: current url={current_url}"
    print(current_url)

    try:
        products = driver.find_elements(By.CLASS_NAME, value="cart_item")
        num_selected_product_actual = len(products)
    except NoSuchElementException:
        num_selected_product_actual = 0
        products = []
    assert num_selected_product == str(num_selected_product_actual), f"Num products in the overview incorrect: Actual={str(num_selected_product_actual)}, Expected={num_selected_product}"

    total_price = 0
    for product in products:
        price_element = product.find_element(By.CLASS_NAME, value="inventory_item_price")
        price = float(price_element.text.strip().replace('$', ''))
        print(f"price: {price}")
        total_price += price

    total_price_element = driver.find_element(By.CLASS_NAME, value="summary_subtotal_label")
    total_price_actual = total_price_element.text.strip().split(':')[1].strip()
    tax_element = driver.find_element(By.CLASS_NAME, value="summary_tax_label")
    final_price_element = driver.find_element(By.XPATH, value="//*[@id='checkout_summary_container']/div/div[2]/div[8]")
    tax = float(tax_element.text.strip().split(':')[1].replace('$', ''))
    final_price_actual = final_price_element.text.strip().split(':')[1].strip()
    final_price = total_price + tax
    total_price_expected = '$' + str(round(total_price, 2))
    final_price_expected = '$' + str(round(final_price, 2))
    assert total_price_actual == total_price_expected, f"Item total price in the overview incorrect: Actual={total_price_actual}, Expected={total_price_expected}"
    assert final_price_actual == final_price_expected, f"Total price in the overview incorrect: Actual={final_price_actual}, Expected={final_price_expected}"

    finish_btn = driver.find_element(By.ID, value="finish")
    finish_btn.click()
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "checkout_complete_container")))
    sleep(const.TIME_WAIT_AFTER_ACTION)
    checkout_complete_container = driver.find_element(By.ID, value="checkout_complete_container")
    current_url = driver.current_url
    is_displayed = checkout_complete_container.is_displayed()
    assert current_url == const.CHECKOUT_FINISH_URL and is_displayed, f"Not show finish page: current url={current_url}, is_displayed={is_displayed}"
    print(current_url)

    back_to_products_btn = driver.find_element(By.ID, value="back-to-products")
    back_to_products_btn.click()
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "inventory_container")))
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    assert current_url == const.INVENTORY_URL, f"Not back to inventory page: current url={current_url}"
    print(current_url)
