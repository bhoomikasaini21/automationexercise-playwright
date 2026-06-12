from pages.login_page import LoginPage
from pages.home_page import HomePage
from testdata.users import VALID_USERS

from utils.screenshot_helper import capture

def test_user_log_in(page):
    home = HomePage(page)
    login = LoginPage(page)

    home.click_signup_login()

    login.enter_login_email(VALID_USERS["email"])
    login.enter_login_password(VALID_USERS["password"])

    capture(page, "before_login")
    
    login.click_login_button()

    capture(page, "after_login")

    print(page.url)

    assert "Logged in as" in page.content()



    