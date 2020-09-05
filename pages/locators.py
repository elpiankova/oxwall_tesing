from selenium.webdriver.common.by import By

# MAIN MENU LOCATORS
class MainPageLocators:
    SIGN_IN_MENU = By.CLASS_NAME, "ow_signin_label"

# USER LOGIN LOCATORS



class DashboardLocators:
    """A class for dashboard page locators. All dashboard page locators should come here"""
    POST_TEXT_FIELD = (By.NAME, "status")
    SEND_BUTTON = (By.NAME, "save")
    POST_TEXT =(By.CSS_SELECTOR, ".ow_newsfeed_content")
    MESSAGE = (By.CLASS_NAME, "ow_message_node")
