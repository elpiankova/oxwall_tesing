from pytest_bdd import scenario
from bdd_tests.posts_steps import *


@scenario("posts.feature", "Create text post (without photos)")
def test_add_post():
    pass


@scenario("posts.feature", "Delete post")
def test_delete_post():
    pass

