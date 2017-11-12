# -*- coding: utf-8 -*-
import os
import time
import unittest
import urllib
from selenium import webdriver
from pages import login_page, finance_page, base_page, base_page_with_table


__author__ = 'Sasha Kurapin'


class FinanceTestSuite(unittest.TestCase):
    """
    Test suite for testing Finance module

    Execute in terminal with a command :

    export MYURL="Environment URL" && chromedriver_url="chromedriver path" && python -m unittest finance_test_suite.FinanceTestSuite
    """
    env_url = os.getenv('MYURL')
    chrome_driver_path = os.getenv('chromedriver_url')
    # env_url = 'https://auto-qa-kur1.joinposter.com'
    print env_url

    def setUp(self):
        self.driver = webdriver.Chrome(self.chrome_driver_path) # temp solution - chrome executable should be in PATH
        self.driver.get(self.env_url) # url should be exported for testing on differnt test envs

    def test_add_new_account(self):
        """
        test scenario: login existing user, select finance menu, add new account, verify that acc was added
        """
        # setup
        login = login_page.LoginPage(self.driver)
        login.login_existing_user('flask+1@i.ua', 'auto_qa_kur1')
        menu = base_page_with_table.BasePageWithTable(self.driver)
        menu.select_finance_menu_item()
        finance_menu = finance_page.FinancePage(self.driver)
        finance_menu.add_account('acc1', 1, 1, 100, 200)
        self.assertTrue(finance_menu.message_success())


    def test_edit_account(self):
        """
        test scenario: login existing user, select finance menu, edit account account (index of account is temp solution), verify that acc was changed
        """
        login = login_page.LoginPage(self.driver)
        login.login_existing_user('flask+1@i.ua', 'auto_qa_kur1')
        menu = base_page_with_table.BasePageWithTable(self.driver)
        menu.select_finance_menu_item()
        finance_menu = finance_page.FinancePage(self.driver)
        finance_menu.edit_account(0,'acc1', 1, 1, 100)
        self.assertTrue(finance_menu.message_success())

    def test_delete_account(self):
        """
        test scenario: login existing user, select finance menu, delete account, verify that acc was deleted
        """
        login = login_page.LoginPage(self.driver)
        login.login_existing_user('flask+1@i.ua', 'auto_qa_kur1')
        menu = base_page_with_table.BasePageWithTable(self.driver)
        menu.select_finance_menu_item()
        finance_menu = finance_page.FinancePage(self.driver)
        finance_menu.delete_account_confirm(1)
        self.assertTrue(finance_menu.message_success())
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
