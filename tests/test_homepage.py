from utils.screenshot_helper import capture

def test_home_page_loaded(page):

    assert page.title() == "Automation Exercise"

    capture(page, "home_page")