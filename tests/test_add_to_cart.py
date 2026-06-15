from pages.cart_page import CartPage
from pages.products_page import ProductsPage

from utils.screenshot_helper import capture

def test_user_can_add_to_cart(page):

    cart = CartPage(page)
    products = ProductsPage(page)

    products.open_product()
    products.add_first_product_to_cart()
    capture(page,"product_added")

    products.view_cart()
    capture(page, "cart_page")

    print (f"Product:{cart.get_product_name()}")
    print(f"Price:{cart.get_product_price()}")
    print(f"Quantity:{cart.get_product_quantity()}")

    assert (cart.get_product_quantity() == "1")
