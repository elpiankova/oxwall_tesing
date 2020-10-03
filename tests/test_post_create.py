# from oxwall_helper import OxwallSite
import time
import pytest
import json
import os.path
import allure
from data.random_string import random_string

from conftest import PROJECT_DIR
from pages.dashboard_page import DashboardPage


with open(os.path.join(PROJECT_DIR, "data", "posts.json"), encoding="utf8") as f:
    post_text_list = json.load(f)

post_text_list.append(random_string(maxlen=1024, spaces=True, enter=True, cyr=True))


@allure.title("Post create test")
@allure.feature("Post feature")
@allure.story("Create text post (without photos)")
@pytest.mark.regresssion
@pytest.mark.parametrize("input_text",  post_text_list)
def test_text_post_create_positive(dashboard_page, logged_user, input_text, db):
    with allure.step("GIVEN initial amount of post in Oxwall database"):
        dashboard_page.is_this_page()
        number_of_posts = dashboard_page.count_posts()
    with allure.step(f'WHEN I add a new post with "{input_text}" in Dashboard page'):
        dashboard_page.create_new_post(input_text)
        posts = dashboard_page.wait_new_post(number_of_posts)
    # Verification new post
    with allure.step(f'THEN this post block has this {input_text} '
                     f'and author {logged_user.real_name} and time "within 1 minute"'):
        assert db.get_last_text_post() == input_text
        assert posts[0].text == input_text.replace('\n', "\r\n")
        assert posts[0].time == "within 1 minute"
        assert posts[0].user == logged_user

    # app = OxwallSite(driver)
    # input_text = "22222New text for post22222222!"
    #
    # number_of_posts = app.count_posts()
    # app.create_new_post(input_text)
    # posts = app.wait_new_post(number_of_posts)
    # # Verification new post
    # assert posts[0].text == input_text


@allure.title("Post delete test")
@allure.feature("Post feature")
@allure.story("Delete text post (without photos)")
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_empty_post_create_negative(driver, logged_user):
    dashboard_page = DashboardPage(driver)
    dashboard_page.new_post_textfield.send_keys("hjbjhbj")

    number_of_old_posts = len(dashboard_page.posts)
    dashboard_page.create_new_post(input_text="")
    assert dashboard_page.message.text == "PLEASE FILL THE FORM PROPERLY"
    time.sleep(2)
    number_of_new_posts = len(dashboard_page.posts)
    assert number_of_new_posts == number_of_old_posts
