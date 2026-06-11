from pages.account_creation_page import AccountcreationPage
from utils.screenshot_helper import capture

def test_account_info_page(page):

    account = AccountcreationPage(page)

    print(
        page.locator("#password").count()
    )
    print(page.url)

    capture(page, "current_page")
    assert page.locator(
        "#password"
    ).count() == 1