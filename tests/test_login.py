def test_login_positive(driver, main_page, login_page, dashboard_page, user):
    # user = {
    #     "username": "admin",
    #     "password":  "pass",
    #     "real_name": "Admin"
    # }

    main_page.sign_in_menu.click()
    assert login_page.is_this_page()
    login_page.fill_form(user.username, user.password)
    login_page.submit_form()
    assert login_page.message.text == "AUTHENTICATION SUCCESS, PLEASE WAIT..."
    assert "info" in login_page.message.get_attribute("class").split(" ")
    assert "rgb(54, 208, 174)" in login_page.message.value_of_css_property("background")
    # assert "error" in login_page.message.get_attribute("class").split(" ") # for negative test
    assert login_page.wait_authentication()
    assert dashboard_page.is_this_page()
    assert dashboard_page.user == user
    # assert dashboard_page.user_menu.get_attribute("href").split("/")[-1] == user.username
    # dashboard_page.logout()
    # asassert main_page.is_this_page()
