from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from base_page import BasePage

__author__ = 'Sasha Kurapin'


class BasePageWithTable(BasePage):
    """
    Template for pages with with items table
    """
    def __init__(self, driver):
        super(BasePageWithTable, self).__init__(driver)

    # def select_finance_menu_item(self):
    #     super(BasePageWithTable, self).select_finance_menu_item(self)

    def quick_search(self, search_word):
    	"""send data to search field 

    	"""
    	pass

    def get_items_count(self):
    	"""
    	:return: return int
    	"""
    	pass

    def get_item_description(self):
    	"""
		:return: return list
    	"""
    	pass

    def page_loaded(self):
        WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.element_to_be_clickable(FinancePageLocators.ADD_ACCOUNT)
        )