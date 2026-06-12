from pages.home_page import HomePage
from pages.login_page import LoginPage


def view_products(logged_in_user):

    page = logged_in_user(page)
    home = HomePage(page)

    home.view_products()

    assert "products" in page.url.lower()
    