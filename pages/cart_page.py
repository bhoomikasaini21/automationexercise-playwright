from locators.cart_locators import CartLocators

class CartPage:
    
    def __init__(self,page):
        self.page = page

    def get_product_name(self):
        return self.page.locator(CartLocators.PRODUCT_NAME).text_content()

    def get_product_price(self):
        return self.page.locator(CartLocators.PRODUCT_PRICE).text_content()

    def get_product_quantity(self):
        return self.page.locator(CartLocators.PRODUCT_QUANTITY).text_content()



