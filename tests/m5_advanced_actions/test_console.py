from playwright.sync_api import Page, expect, BrowserType
from tests.utils.constants import BASE_URL
import pytest, logging


@pytest.fixture
def page(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=2000).new_page()
    yield page
    page.close()
    
def check_console_event(event):
    if event.type == 'error':
        raise AssertionError(f'Console error found:{event.text}')
    
def test_check_console(page: Page):    
    print('')
    # page.on('console', lambda msg: print(msg.text))
    # page.on('pageerror', lambda msg: print(msg))
    page.on('console', lambda msg: check_console_event)
    
    page.goto(BASE_URL)
    first_name = page.get_by_label('First name')
    first_name.fill('Stevan')
    
    console_errors = []
    page.on('console', lambda msg: console_errors.append(msg.text) if msg.type =='error'else None)

    page.get_by_role('button', name='Register').click()
    assert len(console_errors) == 0, 'Expected 0 console errors'


def test_check_console_error(page: Page):
    if event.type == 'error':
        raise AssertionError(f'Console error found:{event.text}')
