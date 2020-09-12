import pytest
from selenium import webdriver
# from oxwall_helper import OxwallSite
from pages.dashboard_page import DashboardPage
from pages.main_page import MainPage
from pages.signin_page import SignInWindow


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(5)
    driver.get("http://127.0.0.1/oxwall/")
    yield driver
    driver.quit()


@pytest.fixture()
def logged_user(driver):
    username = "admin"
    main_page = MainPage(driver)
    main_page.sign_in_initiate()
    login_page = SignInWindow(driver)
    login_page.fill_form(username, "pass")
    login_page.submit_form()
    # app = OxwallSite(driver)
    # app.login_as("admin", "pass")
    yield username
    # app.logout()

@pytest.fixture()
def main_page(driver):
    return MainPage(driver)

@pytest.fixture()
def login_page(driver):
    return SignInWindow(driver)

@pytest.fixture()
def dashboard_page(driver):
    return DashboardPage(driver)
