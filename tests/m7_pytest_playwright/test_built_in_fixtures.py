import pytest
from playwright.sync_api import Page, Browser, Playwright
from time import sleep
from tests.utils.constants import BASE_URL

def test_page_fixture(page: Page):
    name_input = page.get_by_label('First name')


def test_different_browsers(playwright: Playwright):
    chromium_page = playwright.chromium.launch().new_context().new_page()
    firefox_page = playwright.firefox.launch(slow_mo=2000, headless=False).new_context().new_page()   

def test_browser(browser: Browser):
    pass

def test_browser_type(is_chromium):
    print('test')
    if is_chromium:
        print('....')
    pytest.skip('Reason...')
    pass


def test_incomplete_fixture_name(playwright: Playwright, page: Page):
    pass



