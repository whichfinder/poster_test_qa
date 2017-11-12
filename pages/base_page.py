from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.action_chains import ActionChains

__author__ = 'Sasha Kurapin'


class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver):
        self.driver = driver
        self.time_to_wait = 45

    def refresh_browser(self):
        self.driver.refresh()

    def add_new_cookie(self, cookie_name, cookie_value, domain):
        self.driver.add_cookie({'name': cookie_name, 'value': cookie_value, 'domain': domain})

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def select_finance_menu_item(self): # refactor to accept any menu item as string
        WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.presence_of_element_located(BasePageLocators.SIDE_MENU)
        )
        menu_item = self.driver.find_element(*BasePageLocators.FINANCE_MENU)
        menu_item.click()
        menu_item = self.driver.find_element(*BasePageLocators.FINANCE_MENU_ACCOUNTS)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_item).perform()
        menu_item.click()

    def _scroll_menu(self):
        pass

    def open_chat(self):
        pass

    def _get_page_name(self):
        pass

    def _verify_preloader(self):
        pass
