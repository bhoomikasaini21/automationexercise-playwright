from pages.home_page import HomePage
from pages.login_page import LoginPage

from testdata.users import VALID_USERS
from utils.screenshot_helper import capture


def test_user_can_logout(page):

    home = HomePage(page)
    login = LoginPage(page)

    home.click_signup_login()

    login.enter_login_email(VALID_USERS["email"])

    login.enter_login_password(VALID_USERS["password"])

    login.click_login_button()

    capture(page, "logged_in")

    home._click_logout_button()

    capture(page, "logged_out")

    assert "login" in page.url.lower()