from pytest_bdd import given, when, then

from value_objects.user import User


@given("I as a logged user")
def logged_user(config, main_page, login_page):
    user = User(**config["admin_user"])
    main_page.sign_in_initiate()
    login_page.fill_form(user.username, user.password)
    login_page.submit_form()
    return user
    # TODO: logout


@given("initial amount of post in Oxwall database")
def initial_posts(dashboard_page):
    number_of_posts = dashboard_page.count_posts()
    return number_of_posts


@when("I add a new post with <input_text> in Dashboard page")
def create_post(dashboard_page, input_text):
    dashboard_page.create_new_post(input_text)


@then("a new post block appears before old table of posts")
def wait_new_post(initial_posts, dashboard_page):
    dashboard_page.wait_new_post(initial_posts)


@then('this post block has this <input_text> and author as this user and time "within 1 minute"')
def verify_post(dashboard_page, input_text, logged_user):
    post = dashboard_page.posts[0]
    assert post.text == input_text.replace('\n', "\r\n")
    assert post.time == "within 1 minute"
    assert post.user == logged_user
