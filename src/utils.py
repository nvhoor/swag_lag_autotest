from urllib.parse import urlparse, urlunparse


def get_cleaned_url(driver):
    current_url = driver.current_url
    return current_url.split('?')[0]
