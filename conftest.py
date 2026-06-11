import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import BASE_URL

@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            #slow_mo=500
        )

        page = browser.new_page()

        page.set_viewport_size({
            "width": 1920,
            "height": 1080
        })

        page.goto(BASE_URL)

        yield page

        browser.close()