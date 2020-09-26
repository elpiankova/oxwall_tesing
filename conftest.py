import json
import os.path

import pytest
from selenium import webdriver
# from oxwall_helper import OxwallSite
from db.db_connector import OxwallDB
from pages.dashboard_page import DashboardPage
from pages.main_page import MainPage
from pages.signin_page import SignInWindow
from value_objects.user import User

PROJECT_DIR = os.path.dirname(__file__)


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json",
                     help="Project config file name (json file)")
    # parser.addoption("--config"....)


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    with open(os.path.join(PROJECT_DIR, filename), encoding="utf8") as f:
        return json.load(f)


@pytest.fixture()
def driver(selenium, config, base_url):
    driver = selenium
    # driver.implicitly_wait(5)
    # driver.get(config["base_url"])
    driver.get(base_url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(**config["db"])
    yield db
    db.close()


@pytest.fixture()
def logged_user(driver, config):
    user = User(**config["admin_user"])
    main_page = MainPage(driver)
    main_page.sign_in_initiate()
    login_page = SignInWindow(driver)
    login_page.fill_form(user.username, user.password)
    login_page.submit_form()
    # app = OxwallSite(driver)
    # app.login_as("admin", "pass")
    yield user
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


with open(os.path.join(PROJECT_DIR, "data", "users.json"), encoding="utf8") as f:
    user_list = json.load(f)


@pytest.fixture(params=user_list, ids=[str(u) for u in user_list])
def user(request, db):
    u = User(**request.param)
    if not u.is_admin:
        db.create_user(u)
    yield u
    if not u.is_admin:
        db.delete_user(u)
