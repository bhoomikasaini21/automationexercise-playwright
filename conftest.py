import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import BASE_URL
from pages.home_page import HomePage
from pages.login_page import LoginPage
from testdata.users import VALID_USERS


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            #slow_mo=500
        )

        page = browser.new_page()

        page.set_viewport_size({
            "width": 1920,
            "height": 1080
        })

        page.goto(BASE_URL)

        yield page

        browser.close()

@pytest.fixture
def logged_in_user(page):
    home = HomePage(page)
    login = LoginPage(page)

    home.click_signup_login()
    login.enter_login_email(VALID_USERS["email"])
    login.enter_login_password(VALID_USERS["password"])
    login.click_login_button()

    return page