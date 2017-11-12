from base_page_with_table import BasePageWithTable
from locators.finance_page_locators import FinancePageLocators
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class FinancePage(BasePageWithTable):
    """
    describes finance menu
    """
    def __init__(self, driver):
        super(FinancePage, self).__init__(driver)

    def add_account(self, name, curr_index, type_index, init_balance, acquiring_balance):
    	WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.element_to_be_clickable(FinancePageLocators.ADD_ACCOUNT)
        )
        add_account = self.driver.find_element(*FinancePageLocators.ADD_ACCOUNT)
        add_account.click()
        WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.presence_of_element_located(FinancePageLocators.ACCOUNT_NAME)
        )        
        self._complete_acc_info(name, curr_index, type_index, init_balance, acquiring_balance) # refactor later
        self._submit_acc_info()
        WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.element_to_be_clickable(FinancePageLocators.ADD_ACCOUNT)
        )

    def edit_account(self, entity_index, name, curr_index, type_index, init_balance):
    	WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.element_to_be_clickable(FinancePageLocators.EDIT_ACCOUNT)
        )
        edit_account = self.driver.find_element(*FinancePageLocators.EDIT_ACCOUNT) # fix
        edit_account.click()

        # edit_account = self.driver.find_elements(*FinancePageLocators.ACCOUNT_DROPDOWN)
        # edit_account[entity_index].click()
        self._complete_acc_info(name, curr_index, type_index, init_balance) # refactor later
        self._submit_acc_info()
        WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.element_to_be_clickable(FinancePageLocators.ADD_ACCOUNT)
        )

    def _complete_acc_info(self, name, curr_index, type_index, init_balance, *acquiring_balance):
        print name
    	WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.presence_of_element_located(FinancePageLocators.ACCOUNT_NAME)
        )

        name_field = self.driver.find_element(*FinancePageLocators.ACCOUNT_NAME)
        name_field.send_keys(name)
        print "done"
        currency = self.driver.find_element(*FinancePageLocators.ACCOUNT_CURRENCY)
        currency.click()
        currency = self.driver.find_elements(*FinancePageLocators.ACCOUNT_DROPDOWN)
        currency[curr_index].click()
        acc_type = self.driver.find_element(*FinancePageLocators.ACCOUNT_TYPE)
        acc_type.click()
        acc_type = self.driver.find_elements(*FinancePageLocators.ACCOUNT_DROPDOWN)
        acc_type[type_index].click()
        balance = self.driver.find_element(*FinancePageLocators.ACCOUNT_INIT_BALANCE)
        balance.send_keys(init_balance)
        if acquiring_balance:
            print acquiring_balance
            acq_balance = self.driver.find_element(*FinancePageLocators.ACCOUNT_PERCENT_ACQUIRING)
            acq_balance.send_keys(*acquiring_balance)

    def message_success(self):
        WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.presence_of_element_located(FinancePageLocators.MESSAGE_SUCCESS)
        )
    	message = self.driver.find_element(*FinancePageLocators.MESSAGE_SUCCESS)
        print "finding success message"
    	return message.is_displayed()
    	
    def _submit_acc_info(self):
    	submit = self.driver.find_element(*FinancePageLocators.ACCOUNT_SUBMIT)
        print "click submit"
    	submit.click()
    	

    def delete_account_confirm(self, index):
        WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.presence_of_element_located(FinancePageLocators.MORE_ACTIONS)
        )
    	delete_account = self.driver.find_elements(*FinancePageLocators.MORE_ACTIONS)
        print "finding list more actions"
    	delete_account[index].click()
        delete_button = self.driver.find_elements(*FinancePageLocators.MORE_ACTIONS_DELETE_ACCOUNT)
        for element in delete_button:
            if element.is_displayed():
            	element.click()
                print "click delete"
            	WebDriverWait(self.driver, self.time_to_wait).until(
                        expected_conditions.element_to_be_clickable(FinancePageLocators.CONFIRM_DELETE)
                )
                confirm = self.driver.find_element(*FinancePageLocators.CONFIRM_DELETE)
                print "confirm delete"
                confirm.click()


    def delete_account_cancel(self):
    	delete_account = self.driver.find_elements(*FinancePageLocators.MORE_ACTIONS)
    	delete_account[index].click()
        find_element(*FinancePageLocators.MORE_ACTIONS_DELETE_ACCOUNT)
    	delete_account.click()
    	WebDriverWait(self.driver, self.time_to_wait).until(
                expected_conditions.presence_of_element_located(*FinancePageLocators.ADD_ACCOUNT)
        )
        cancel = self.driver.find_element(*FinancePageLocators.CANCEL_DELETE)
        cancel.click()
    