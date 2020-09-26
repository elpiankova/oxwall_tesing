from pages.locators import PostLocator
from value_objects.user import User


class PostBlock:
    def __init__(self, element):
        self.element = element

    @property
    def text(self):
        return self.element.find_element(*PostLocator.POST_TEXT).text

    @property
    def time(self):
        return self.element.find_element(*PostLocator.POST_TIME).text

    @property
    def user(self):
        user_element = self.element.find_element(*PostLocator.POST_USER)
        username = user_element.get_attribute("href").split("/")[-1]
        real_name = user_element.text
        return User(username=username, real_name=real_name)

    # TODO
    # @property
    # def likes_count(self):
    #     return None
    #
    # def add_like(self):
    #     self.likes_bt.click()
    #
    # def add_comment(self, text):
