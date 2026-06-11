from pages.account_creation_page import AccountcreationPage
from pages.home_page import HomePage
from pages.signup_page import SignupPage

from utils.random_generator import generate_email
from utils.screenshot_helper import capture


def test_user_can_open_signup(page):

    home = HomePage(page)
    signup = SignupPage(page)

    home.click_signup_login()
    email = generate_email()

    page.wait_for_load_state("networkidle")

    page.wait_for_selector('[data-qa="signup-name"]')

    signup.enter_name("Test User")
    signup.enter_email(email)

    capture(page, "before_signup")

    signup.click_signup()

    capture(page, "after_signup")

    assert "signup" in page.url.lower()

    account = AccountcreationPage(page)

    account.select_title()
    account.enter_password("Password123")
    account.select_dob()

    account.enter_first_name("Test")
    account.enter_last_name("User")
    account.enter_company("ABC Pvt Ltd")
    account.enter_address("Street 1")
    account.enter_address2("Near Market")

    account.select_country()

    account.enter_state("Himachal Pradesh")
    account.enter_city("Solan")
    account.enter_zipcode("173212")
    account.enter_mobile_number("9876543210")

    capture(page, "before_create_account")

    account.click_create_account()

    capture(page, "account_created")

    assert "Account Created!" in account.get_account_created_text()
    account.click_continue()