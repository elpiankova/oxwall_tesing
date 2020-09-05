from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import MainPageLocators
from pages.page import Page
from pages.signin_page import SignInWindow


class MainPage(Page):

    def sign_in_initiate(self):
        sign_in_menu = self.driver.find_element(*MainPageLocators.SIGN_IN_MENU)
        sign_in_menu.click()
        return SignInWindow(self.driver)
