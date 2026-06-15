from pages.products_page import ProductsPage


def test_view_products(logged_in_user):

    page = logged_in_user
    product = ProductsPage(page)

    product.open_product()

    assert "products" in page.url.lower()
    