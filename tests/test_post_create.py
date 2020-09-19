# from oxwall_helper import OxwallSite
import time
import pytest
import json
import os.path
from data.random_string import random_string

from conftest import PROJECT_DIR
from pages.dashboard_page import DashboardPage


with open(os.path.join(PROJECT_DIR, "data", "posts.json"), encoding="utf8") as f:
    post_text_list = json.load(f)

post_text_list.append(random_string(maxlen=1024, spaces=True, enter=True, cyr=True))


@pytest.mark.parametrize("input_text",  post_text_list)
def test_text_post_create_positive(driver, logged_user, input_text):

    dashboard_page = DashboardPage(driver)
    dashboard_page.is_this_page()
    number_of_posts = dashboard_page.count_posts()
    dashboard_page.create_new_post(input_text)
    posts = dashboard_page.wait_new_post(number_of_posts)
    # Verification new post
    assert posts[0].text == input_text
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


def test_empty_post_create(driver, logged_user):
    dashboard_page = DashboardPage(driver)
    dashboard_page.new_post_textfield.send_keys("hjbjhbj")

    number_of_old_posts = len(dashboard_page.posts)
    dashboard_page.create_new_post(input_text="")
    assert dashboard_page.message.text == "PLEASE FILL THE FORM PROPERLY"
    time.sleep(2)
    number_of_new_posts = len(dashboard_page.posts)
    assert number_of_new_posts == number_of_old_posts
