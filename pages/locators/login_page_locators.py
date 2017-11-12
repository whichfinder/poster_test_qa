from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGIN_EMAIL = (By.ID, 'email')
    LOGIN_PWD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-green')

