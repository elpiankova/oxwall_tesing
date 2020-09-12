from pages.locators import InternalPageLocators
from pages.page import Page


class InternalPage(Page):
    @property
    def sign_in_menu(self):
        return self.find_element(InternalPageLocators.SIGN_IN_MENU)

    @property
    def dashboard_menu(self):
        return self.find_element(InternalPageLocators.DASH_MENU)

    @property
    def main_menu(self):
        return self.find_element(InternalPageLocators.MAIN_MENU)

    @property
    def user_menu(self):
        return self.find_element(InternalPageLocators.USER_MENU)

    def sign_in_initiate(self):
        self.sign_in_menu.click()

    # TODO
    def logout(self):
        pass
