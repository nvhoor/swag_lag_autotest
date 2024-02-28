import datetime
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src import const


def test_login(driver: ChromiumDriver, username, password):
    current_url = driver.current_url
    assert current_url == const.BASE_URL, f"Can't enter this website: baseurl={const.BASE_URL}, current url={current_url}"
    print(current_url)
    text_box_username = driver.find_element(by=By.NAME, value="user-name")
    text_box_username.send_keys(username)

    text_box_password = driver.find_element(by=By.NAME, value="password")
    text_box_password.send_keys(password)
    submit_button = driver.find_element(by=By.NAME, value="login-button")
    submit_button.click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "inventory_container")))
    sleep(const.TIME_WAIT_AFTER_ACTION)
    current_url = driver.current_url
    print(current_url)
    assert current_url == const.INVENTORY_URL, f"Login fail, current_url={current_url}"


def test_logout(driver: ChromiumDriver):
    current_url = driver.current_url
    assert current_url == const.INVENTORY_URL, f"Not on inventory page: current url={current_url}"
    print(current_url)
    react_burger_menu_btn = driver.find_element(by=By.ID, value="react-burger-menu-btn")
    react_burger_menu_btn.click()
    WebDriverWait(driver, 2.0).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    sleep(const.TIME_WAIT_AFTER_ACTION)
    logout_sidebar_link = driver.find_element(by=By.ID, value="logout_sidebar_link")
    logout_sidebar_link.click()
    current_url = driver.current_url
    assert current_url == const.BASE_URL, f"Can't logout: baseurl={const.BASE_URL}, current url={current_url}"
    print(current_url)

