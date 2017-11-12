from selenium.webdriver.common.by import By

class FinancePageLocators(object):
	ADD_ACCOUNT = (By.CSS_SELECTOR, 'a[href="/manage/finance/accounts/add_account"]')
	EDIT_ACCOUNT = (By.CSS_SELECTOR, '.edit.noprint-cell')
	MORE_ACTIONS = (By.CSS_SELECTOR, 'button[class="btn btn-edit-ellipsis dropdown-toggle"]')
	MORE_ACTIONS_DELETE_ACCOUNT = (By.CSS_SELECTOR, '.pseudo-link.delete-book-account')

	MODAL_WINDOW = (By.CSS_SELECTOR, '.modal-dialog')
	CONFIRM_DELETE = (By.CSS_SELECTOR, '.btn.btn-green.btn-confirm')
	CANCEL_DELETE = (By.CSS_SELECTOR, 'button[data-dismiss="modal"]')

	ACCOUNT_NAME = (By.CSS_SELECTOR, 'input[name="name"]')
	ACCOUNT_CURRENCY = (By.CSS_SELECTOR, 'select[name="currency_id"]')
	ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, 'select[name="currency_id"] option')
	ACCOUNT_TYPE = (By.CSS_SELECTOR, 'select[name="type"]')
	ACCOUNT_INIT_BALANCE = (By.CSS_SELECTOR, 'input[name="balance_start"]')
	ACCOUNT_PERCENT_ACQUIRING = (By.CSS_SELECTOR, 'input[name="percent_acquiring"]')
	ACCOUNT_SUBMIT = (By.CSS_SELECTOR, '.btn.btn-green.btn-lg')

	MESSAGE_SUCCESS = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissable')