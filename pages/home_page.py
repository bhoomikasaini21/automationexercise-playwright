from locators.home_locators import HomeLocators
class HomePage:

    def __init__(self, page):
        self.page = page

    def click_signup_login(self):
        self.page.locator(
            HomeLocators.SIGNUP_LOGIN
        ).click()