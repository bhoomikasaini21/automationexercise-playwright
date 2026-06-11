from locators.account_creation_locators import AccountcreationLocators

class AccountcreationPage:

    def __init__(self,page):
        self.page = page

    def select_title(self):
        self.page.locator(AccountcreationLocators.TITLE_MR).check()

    def enter_password(self,password):
        self.page.locator(AccountcreationLocators.PASSWORD).fill(password)

    def select_dob(self):
        self.page.select_option(AccountcreationLocators.DAY, "10")

        self.page.select_option(AccountcreationLocators.MONTH, "5")

        self.page.select_option(AccountcreationLocators.YEAR, "1995")

    def enter_first_name(self,first_name):
        self.page.locator(AccountcreationLocators.FIRST_NAME).fill(first_name)

    def enter_last_name(self,last_name):
        self.page.locator(AccountcreationLocators.LAST_NAME).fill(last_name)

    def enter_company(self,company):
        self.page.locator(AccountcreationLocators.COMPANY).fill(company)

    def enter_address(self,address):
        self.page.locator(AccountcreationLocators.ADDRESS).fill(address)

    def enter_address2(self,address2):
        self.page.locator(AccountcreationLocators.ADDRESS2).fill(address2)

    def select_country(self):
        self.page.select_option(AccountcreationLocators.COUNTRY, "India")

    def enter_state(self,state):
        self.page.locator(AccountcreationLocators.STATE).fill(state)

    def enter_city(self,city):
        self.page.locator(AccountcreationLocators.CITY).fill(city)

    def enter_zipcode(self,zipcode):
        self.page.locator(AccountcreationLocators.ZIP_CODE).fill(zipcode)

    def enter_mobile_number(self,mobile_number):
        self.page.locator(AccountcreationLocators.MOBILE_NUMBER).fill(mobile_number)

    def click_create_account(self):
        self.page.locator(AccountcreationLocators.CREATE_ACCOUNT).click()

    
    def get_account_created_text(self):
        return self.page.locator(AccountcreationLocators.ACCOUNT_CREATED).text_content()
    
    def click_continue(self):
        self.page.locator('[data-qa="continue-button"]').click()
    