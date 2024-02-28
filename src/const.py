from urllib.parse import urljoin

BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = urljoin(BASE_URL, "inventory.html")
CART_URL = urljoin(BASE_URL, "cart.html")
DETAIL_URL = urljoin(BASE_URL, "inventory-item.html")
CHECKOUT_INFO_URL = urljoin(BASE_URL, "checkout-step-one.html")
CHECKOUT_OVERVIEW_URL = urljoin(BASE_URL, "checkout-step-two.html")
CHECKOUT_FINISH_URL = urljoin(BASE_URL, "checkout-complete.html")

TIME_WAIT_AFTER_ACTION = 0
IMPLICITLY_WAIT = 0
