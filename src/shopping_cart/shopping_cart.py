from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src import const, utils


# Test case: sheet 'Shopping cart' => caseId: 6
def test_add_something_to_cart(driver: ChromiumDriver):
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
    num_selected_product = int(num_selected_products_actual)

    first_add_to_card_button = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/button')
    first_add_to_card_button.click()
    sleep(const.TIME_WAIT_AFTER_ACTION)
    first_add_to_card_button = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/button')
    new_text = first_add_to_card_button.text
    shopping_cart_badge = driver.find_element(By.CLASS_NAME, value="shopping_cart_badge")
    num_selected_products_actual = shopping_cart_badge.text
    assert new_text == "Remove", "Add to cart button not update to Remove button."
    num_selected_product += 1
    assert num_selected_products_actual == str(num_selected_product), f"Shopping cart badge show incorrect number selected products. Expected={num_selected_product}, Actual={num_selected_products_actual}"

    elements = driver.find_elements(By.CLASS_NAME, value="inventory_item")
    num_products = len(elements)
    last_add_to_card_button = driver.find_element(by=By.XPATH, value=f'//*[@id="inventory_container"]/div/div[{num_products}]/div[2]/div[2]/button')
    last_add_to_card_button.click()
    sleep(const.TIME_WAIT_AFTER_ACTION)
    first_add_to_card_button = driver.find_element(by=By.XPATH, value=f'//*[@id="inventory_container"]/div/div[{num_products}]/div[2]/div[2]/button')
    new_text = first_add_to_card_button.text
    shopping_cart_badge = driver.find_element(By.CLASS_NAME, value="shopping_cart_badge")
    num_selected_products_actual = shopping_cart_badge.text
    assert new_text == "Remove", "Add to cart button not update to Remove button."
    num_selected_product += 1
    assert num_selected_products_actual == str(num_selected_product), f"Shopping cart badge show in correct number selected products. Expected={num_selected_product}, Actual={num_selected_products_actual}"

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
    assert num_selected_products_actual == str(num_selected_product), "Shopping cart badge show in correct number selected products. Expected={num_selected_product}, Actual={num_selected_products_actual}"
    checkout_btn = driver.find_element(By.ID, value="checkout")
    is_enabled = checkout_btn.is_enabled()
    assert is_enabled, f"Checkout button not enabled."

    continue_shopping_btn = driver.find_element(By.ID, value="continue-shopping")
    continue_shopping_btn.click()
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "inventory_container")))
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    assert current_url == const.INVENTORY_URL, f"Can't back to inventory page: current url={current_url}"
    print(current_url)
    shopping_cart_badge = driver.find_element(By.CLASS_NAME, value="shopping_cart_badge")
    num_selected_product = shopping_cart_badge.text
    assert num_selected_products_actual == str(num_selected_product), "Shopping cart badge show in correct number selected products. Expected={num_selected_product}, Actual={num_selected_products_actual}"

    first_add_to_card_button = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/button')
    first_btn_text = first_add_to_card_button.text
    last_add_to_card_button = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/button')
    last_btn_text = last_add_to_card_button.text
    assert first_btn_text == "Remove", "First 'Add to cart' button not update to Remove button."
    assert last_btn_text == "Remove", "Last 'Add to cart' button not update to Remove button."


def test_add_something_from_product_detail_page(driver: ChromiumDriver):
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
    num_selected_product = int(num_selected_products_actual)

    product_img = driver.find_element(by=By.XPATH, value=f'//*[@id="inventory_container"]/div/div[2]/div[1]')
    product_img.click()
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "inventory_item_container")))
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = utils.get_cleaned_url(driver)
    assert current_url == const.DETAIL_URL, f"Not on product detail page: current url={current_url}"
    print(current_url)

    add_to_card_button = driver.find_element(by=By.XPATH, value='//*[@id="inventory_item_container"]/div/div/div[2]/button')
    add_to_card_button.click()
    sleep(const.TIME_WAIT_AFTER_ACTION)
    add_to_card_button = driver.find_element(by=By.XPATH, value='//*[@id="inventory_item_container"]/div/div/div[2]/button')
    btn_text = add_to_card_button.text
    shopping_cart_badge = driver.find_element(By.CLASS_NAME, value="shopping_cart_badge")
    num_selected_products_actual = shopping_cart_badge.text
    assert btn_text == "Remove", "Add to cart button not update to Remove button."
    num_selected_product += 1
    assert num_selected_products_actual == str(num_selected_product), f"Shopping cart badge show incorrect number selected products. Expected={num_selected_product}, Actual={num_selected_products_actual}"

    back_to_products_link = driver.find_element(By.ID, value="back-to-products")
    back_to_products_link.click()
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "inventory_container")))
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    assert current_url == const.INVENTORY_URL, f"Can't back to inventory page: current url={current_url}"
    print(current_url)

    add_to_card_button = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/button')
    btn_text = add_to_card_button.text
    assert btn_text == "Remove", "Second 'Add to cart' button not update to Remove button."


def test_remove_product_from_cart(driver: ChromiumDriver):
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
    num_selected_product = int(num_selected_products_actual)

