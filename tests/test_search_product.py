from pages.products_page import ProductsPage

from utils.screenshot_helper import capture

def test_user_can_search_product(page):
    products = ProductsPage(page)

    products.open_product()

    products.search_product("Blue Top")
    capture(page, "searched_product")

    results = products.get_searched_product()
    print(results)

    assert page.locator( "text = Searched Products").is_visible()
