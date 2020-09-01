import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(5)
    driver.get("http://127.0.0.1/oxwall/")
    yield driver
    driver.quit()


@pytest.fixture()
def wait(driver):
    return WebDriverWait(driver, 5)


@pytest.fixture()
def login(driver, wait):
    # Login
    sign_in_menu = driver.find_element(By.CLASS_NAME, "ow_signin_label")
    sign_in_menu.click()
    user_name = driver.find_element(By.NAME, "identity")
    user_name.clear()
    user_name.send_keys("admin")
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("pass")
    sign_in_button = driver.find_element(By.NAME, "submit")
    sign_in_button.click()
    # Wait Dashboard page
    wait.until(presence_of_element_located((By.CSS_SELECTOR, ".base_dashboard.active")),
               message="Dashboard page doesn't open")
    yield
    # Logout
