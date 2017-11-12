from selenium.webdriver.common.by import By


class BasePageLocators(object):
    SIDE_MENU = (By.CLASS_NAME, 'side-menu')
    FINANCE_MENU = (By.CSS_SELECTOR, 'img[src="/i/manage/side-menu/finance.svg"]')
    FINANCE_MENU_ACCOUNTS = (By.CSS_SELECTOR, 'a[href="/manage/finance/accounts"]')
    PRELOADER = (By.CSS_SELECTOR, '')
    
