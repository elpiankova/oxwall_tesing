from pages.locators import InternalPageLocators
from pages.page import Page
from value_objects.user import User


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
    def user(self):
        el = self.find_element(InternalPageLocators.USER_MENU)
        user = User(username=el.get_attribute("href").split("/")[-1], real_name=el.text)
        return user

    def sign_in_initiate(self):
        self.sign_in_menu.click()

    # TODO
    def logout(self):
        pass
