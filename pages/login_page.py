from base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.common.action_chains import ActionChains

__author__ = 'Sasha Kurapin'


class LoginPage(BasePage):
    """
    describes login page
    """
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def login_existing_user(self, login_email, login_pwd):
        """login existing user
        :param login_email: 
        :param login pwd:
        
        """
        WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_EMAIL)
        )
        print 'signin page is present'
        email_field = self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_field.send_keys(login_email)
        print 'email was entered'
        pass_field = self.driver.find_element(*LoginPageLocators.LOGIN_PWD)
        pass_field.send_keys(login_pwd)
        print 'password was entered'
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        print 'signin button was clicked'

    def forget_password_click(self):
        pass

    def click_tech_support_click(self):
        pass