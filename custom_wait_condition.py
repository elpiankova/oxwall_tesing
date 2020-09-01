from selenium.webdriver.common.by import By


def presence_of_11_elements_located(driver):
    posts = driver.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content")
    if len(posts) == 11:
        return posts
    else:
        return False


def presence_of_N_elements_located_(locator, number):
    def method(driver):
        posts = driver.find_elements(*locator)
        if len(posts) == number:
            return posts
        else:
            return False
    return method


class presence_of_N_elements_located:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        posts = driver.find_elements(*self.locator)
        if len(posts) == self.number and posts[0].is_displayed():
            return posts
        else:
            return False


class A:
    def __init__(self, x):
        self.x = x

    def __call__(self, n):
        return n ** self.x


a = A(2)
b = A(3)

print(a(2))
print(a(10))
print(b(10))
print()
