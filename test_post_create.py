# from oxwall_helper import OxwallSite
import time

from pages.dashboard_page import DashboardPage


def test_empty_post_create(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.new_post_textfield.send_keys("hjbjhbj")

    number_of_old_posts = len(dashboard_page.posts)
    dashboard_page.create_new_post(input_text="")
    assert dashboard_page.message.text == "PLEASE FILL THE FORM PROPERLY"
    time.sleep(2)
    number_of_new_posts = len(dashboard_page.posts)
    assert number_of_new_posts == number_of_old_posts


def test_text_post_create_positive(driver, login):
    input_text = "New New text for post!"

    dashboard_page = DashboardPage(driver)
    number_of_posts = dashboard_page.count_posts()
    dashboard_page.create_new_post(input_text)
    posts = dashboard_page.wait_new_post(number_of_posts)
    # Verification new post
    assert posts[0].text == input_text

    # app = OxwallSite(driver)
    # input_text = "22222New text for post22222222!"
    #
    # number_of_posts = app.count_posts()
    # app.create_new_post(input_text)
    # posts = app.wait_new_post(number_of_posts)
    # # Verification new post
    # assert posts[0].text == input_text
