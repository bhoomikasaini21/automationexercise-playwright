from pages.home_page import HomePage

def test_user_can_open_login_page(page):

    home = HomePage(page)

    home.click_signup_login()

    assert "login" in page.url.lower()