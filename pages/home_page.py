from locators.home_locators import HomeLocators

class HomePage:

    def __init__(self, page):
        self.page = page

    def click_signup_login(self):
        self.page.locator(HomeLocators.SIGNUP_LOGIN).click()

    def click_logout_button(self):
        self.page.locator(HomeLocators.LOGOUT_BUTTON).click()

    def varify_delete_account(self):
        self.page.locator(HomeLocators.DELETE_ACCOUNT_BUTTON).click()

