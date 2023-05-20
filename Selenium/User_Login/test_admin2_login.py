# Code by foolfor-20230515
from selenium import webdriver
from webtest.user_login import UserLogin


def test_admin2_login():
    user_name = "admin2"
    user_password = "admin2"
    login = UserLogin()
    login.driver = webdriver.Chrome()

    # do login test and get info from new page
    info_str = login.login_return_value(user_name, user_password)

    # close web driver
    login.driver.close()
    assert info_str.index("KEYWORD")
