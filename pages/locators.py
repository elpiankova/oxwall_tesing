from selenium.webdriver.common.by import By

class MainPageLocators:
    """Main page locators"""
    pass

# TODO SignInPage locators


class InternalPageLocators:
    DASH_MENU = (By.CLASS_NAME, "base_dashboard")
    MAIN_MENU = (By.CLASS_NAME, "base_main_menu_index")
    # TODO other menu
    USER_MENU = (By.XPATH, '//div[@class="ow_console_items_wrap"]/div[5]/a')
    # '//a[contains(@id, "user_menu_")]'
    SIGN_IN_MENU = By.CLASS_NAME, "ow_signin_label"


class DashboardLocators:
    """A class for dashboard page locators. All dashboard page locators should come here"""
    HEADER = (By.CSS_SELECTOR, ".ow_stdmargin.ow_ic_house")

    POST_TEXT_FIELD = (By.NAME, "status")
    SEND_BUTTON = (By.NAME, "save")
    POST = (By.XPATH, '//li[contains(@id, "action-feed")]')
    MESSAGE = (By.CLASS_NAME, "ow_message_node")


class PostLocator:
    POST_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    # TODO:
    LIKES_BUTTON = ()
    LIKES_COUNTER = ()
    COMMENTS_COUNTER = ()
    COMMENTS_BUTTON = ()
