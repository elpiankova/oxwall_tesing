import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from custom_wait_condition import presence_of_N_elements_located
from pages.internal_page import InternalPage
from pages.locators import DashboardLocators
from pages.post_block import PostBlock


class DashboardPage(InternalPage):
    @property
    def header(self):
        return self.find_element(DashboardLocators.HEADER)

    @property
    def new_post_textfield(self):
        return self.find_element(DashboardLocators.POST_TEXT_FIELD)

    @property
    def send_button(self):
        return self.find_visible_element(DashboardLocators.SEND_BUTTON)

    @property
    def posts(self) -> list:
        # result = []
        # for element in self.driver.find_elements(*DashboardLocators.POST):
        #     result.append(PostBlock(element))
        # return result
        return [PostBlock(element) for element in self.driver.find_elements(*DashboardLocators.POST)]

    @property
    def message(self) -> WebElement:
        message_element = self.find_visible_element(DashboardLocators.MESSAGE)
        return message_element

    def wait_new_post(self, number_of_posts: int):
        # Wait new post appears
        posts = self.wait.until(
            presence_of_N_elements_located(DashboardLocators.POST, number_of_posts + 1),
            message=f"Does'nt appear {number_of_posts} elements"
        )
        return [PostBlock(el) for el in posts]

    @allure.step('WHEN I add a new post with "{input_text}" in Dashboard page')
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

    def is_this_page(self):
        return ("active" in self.dashboard_menu.get_attribute("class").split()
                and self.header.text == "MY DASHBOARD")
