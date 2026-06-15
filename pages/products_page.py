from locators.products_locators import ProductsLocators

class ProductsPage:

    def __init__(self,page):
        self.page = page

    def open_product(self):
        self.page.locator(ProductsLocators.PRODUCT_MENU).click()

    def view_first_product(self):
        self.page.locator(ProductsLocators.VIEW_PRODUCT).click()

    def view_product_details(self):
         product_name = self.page.locator(ProductsLocators.PRODUCT_NAME).text_content()
         product_category = self.page.locator(ProductsLocators.PRODUCT_CATEGORY).text_content()
         product_price = self.page.locator(ProductsLocators.PRODUCT_PRICE).text_content()

         return product_name, product_category, product_price
    
    def search_product(self,product_name):
        self.page.locator(ProductsLocators.SEARCH_INPUT).fill(product_name)
        self.page.locator(ProductsLocators.SEARCH_BUTTON).click()

    def get_searched_product(self):
       return self.page.locator(ProductsLocators.SEARCHED_PRODUCT_NAME).all_text_contents()


    def add_first_product_to_cart(self):
        self.page.locator(ProductsLocators.FIRST_PRODUCT_ADD_TO_CART).first.click()

    def view_cart(self):
        self.page.locator(ProductsLocators.VIEW_CART).click()