from locators.login_locators import LoginLocators

class LoginPage:

    def __init__(self,page):
        self.page = page

    def enter_login_email(self,login_email):
        self.page.locator(LoginLocators.LOGIN_EMAIL).fill(login_email)

    def enter_login_password(self,login_password):
        self.page.locator(LoginLocators.LOGIN_PASSWORD).fill(login_password)

    def click_login_button(self):
        self.page.locator(LoginLocators.LOGIN_BUTTON).click()

    def get_logged_in_as_button(self):
        self.page.locator(LoginLocators.LOGGED_IN_AS_BUTTON).text_content()

