from pages.products_page import ProductsPage
from utils.screenshot_helper import capture

def test_view_product_details(page):

    products = ProductsPage(page)

    products.open_product()
    capture (page, "product_page")

    products.view_first_product()
    capture (page, "product_details")

    name,category,price = products.view_product_details()
    print("Product Name:", name)
    print("Product Category:", category)
    print("Product Price:", price)

    assert "/product_details" in page.url

      