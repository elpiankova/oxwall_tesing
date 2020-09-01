from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from custom_wait_condition import presence_of_11_elements_located, presence_of_N_elements_located


def test_text_post_create_positive(driver, login, wait):
    input_text = "22222New text for post22222222!"
    # Count posts
    posts = driver.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content")
    number_of_posts = len(posts)

    # Create new post
    # new_post_textfield = driver.find_element(By.NAME, "status")
    new_post_textfield = wait.until(presence_of_element_located((By.NAME, "status")),
                                    message="Post text field doesn't apper")
    new_post_textfield.clear()
    new_post_textfield.send_keys(input_text)

    send_button = driver.find_element(By.NAME, "save")
    send_button.click()

    posts = wait.until(
        presence_of_N_elements_located((By.CSS_SELECTOR, ".ow_newsfeed_content"), number_of_posts+1)
    )
    assert posts[0].text == input_text
