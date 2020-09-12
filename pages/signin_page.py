from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.dashboard_page import DashboardPage
from pages.page import Page


class SignInWindow(Page):
    # TODO: extract locators and other property elements
    @property
    def active_menu(self):
        return self.find_element((By.CLASS_NAME, "active"))

    @property
    def window(self):
        return self.find_element((By.CLASS_NAME, "ow_bg_color"))

    @property
    def header(self):
        return self.find_element((By.CLASS_NAME, "ow_ic_file"))

    @property
    def user_name(self):
        return self.driver.find_element(By.NAME, "identity")

    @property
    def message(self):
        return self.find_visible_element((By.CLASS_NAME, "ow_message_node"))

    def fill_form(self, username, password):
        self.user_name.clear()
        self.user_name.send_keys(username)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)

    def submit_form(self):
        sign_in_button = self.driver.find_element(By.NAME, "submit")
        sign_in_button.click()

    def wait_authentication(self):
        try:
            self.wait.until(EC.staleness_of(self.active_menu),
                            message="Old Page")
            # self.wait.until(EC.staleness_of(self.active_menu),
            #                 message="Old Page")
            # self.wait.until(EC.visibility_of(self.active_menu),
            #                 message="Inner page doesn't open")
            return True
        except TimeoutException:
            return False

    def is_this_page(self):
        return self.window.is_displayed() and self.header.text == "Please sign in"
