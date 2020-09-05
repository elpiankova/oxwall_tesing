from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from custom_wait_condition import presence_of_N_elements_located
from pages.locators import DashboardLocators
from pages.page import Page


class DashboardPage(Page):
    @property
    def new_post_textfield(self):
        return self.find_element(DashboardLocators.POST_TEXT_FIELD)

    @property
    def send_button(self):
        return self.find_visible_element(DashboardLocators.SEND_BUTTON)

    @property
    def posts(self):
        return self.find_elements(DashboardLocators.POST_TEXT)

    @property
    def message(self):
        message_element = self.find_visible_element(DashboardLocators.MESSAGE)
        return message_element


    def wait_new_post(self, number_of_posts):
        # Wait new post appears
        posts = self.wait.until(
            presence_of_N_elements_located(DashboardLocators.POST_TEXT, number_of_posts + 1),
            message=f"Does'nt appear {number_of_posts} elements"
        )
        return posts

    def create_new_post(self, input_text):
        # Create new post
        self.new_post_textfield.click()
        self.new_post_textfield.clear()
        self.new_post_textfield.send_keys(input_text)
        self.send_button.click()

    def count_posts(self):
        # Count posts
        number_of_posts = len(self.posts)
        return number_of_posts


