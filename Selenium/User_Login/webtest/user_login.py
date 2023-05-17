# Code by foolfor-20230515
from selenium.webdriver.common.by import By
from webtest.globalvals import GlobalVals
import time


class UserLogin:
    def __init__(self):
        """Selenium web driver: Chrome, Firefox, Ie, Edge, Safari...
        """
        self.driver = None

    def login_only(self, user_name, user_password):
        """Do something after login.
        """
        # get url
        self.driver.get(GlobalVals.URL)
        time.sleep(5)

        # username
        self.driver.find_element(By.XPATH, GlobalVals.USER_XPATH).send_keys(user_name)
        time.sleep(2)

        # password
        self.driver.find_element(By.XPATH, GlobalVals.PASS_XPATH).send_keys(user_password)
        time.sleep(2)

        # submit
        self.driver.find_element(By.XPATH, GlobalVals.SUBMIT_XPATH).click()
        time.sleep(3)

    def login_return_value(self, user_name, user_password):
        """Login test
        """
        self.login_only(user_name, user_password)

        # find an element of the new page
        info_assert = self.driver.find_element(By.XPATH, GlobalVals.LOGO_XPATH)
        value = info_assert.get_attribute("innerHTML")
        time.sleep(2)
        return value
