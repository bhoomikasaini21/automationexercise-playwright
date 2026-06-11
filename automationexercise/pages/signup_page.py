from locators.signup_locators import SignupLocators
class SignupPage:

    def __init__(self,page):
        self.page = page

    def enter_name(self,name):
        self.page.locator(SignupLocators.NAME).fill(name)

    def enter_email(self,email):
        self.page.locator(SignupLocators.EMAIL).fill(email)

    def click_signup(self):
        self.page.locator(SignupLocators.SIGNUP_BUTTON).click()