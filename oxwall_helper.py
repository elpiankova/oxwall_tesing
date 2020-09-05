from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from custom_wait_condition import presence_of_N_elements_located
from pages.locators import POST_TEXT_FIELD, SEND_BUTTON, POST_TEXT


class OxwallSite:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wait_new_post(self, number_of_posts):
        # Wait new post appears
        posts = self.wait.until(
            presence_of_N_elements_located(POST_TEXT, number_of_posts + 1)
        )
        return posts

    def create_new_post(self, input_text):
        # Create new post
        # new_post_textfield = driver.find_element(By.NAME, "status")
        new_post_textfield = self.wait.until(presence_of_element_located(POST_TEXT_FIELD),
                                             message="Post text field doesn't appear")
        new_post_textfield.clear()
        new_post_textfield.send_keys(input_text)
        send_button = self.driver.find_element(*SEND_BUTTON)
        send_button.click()

    def count_posts(self):
        # Count posts
        posts = self.driver.find_elements(*POST_TEXT)
        number_of_posts = len(posts)
        return number_of_posts

    def login_as(self, username, password):
        # Login
        sign_in_menu = self.driver.find_element(By.CLASS_NAME, "ow_signin_label")
        sign_in_menu.click()
        user_name = self.driver.find_element(By.NAME, "identity")
        user_name.clear()
        user_name.send_keys(username)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)
        sign_in_button = self.driver.find_element(By.NAME, "submit")
        sign_in_button.click()
        # Wait Dashboard page
        self.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".base_dashboard.active")),
                   message="Dashboard page doesn't open")

    def logout(self):
        pass
