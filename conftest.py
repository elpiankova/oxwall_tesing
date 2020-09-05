import pytest
from selenium import webdriver
# from oxwall_helper import OxwallSite
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(5)
    driver.get("http://127.0.0.1/oxwall/")
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_initiate()
    sign_in_page.fill_form("admin", "pass")
    dashboard_page = sign_in_page.submit_form()
    # app = OxwallSite(driver)
    # app.login_as("admin", "pass")
    yield
    # app.logout()
