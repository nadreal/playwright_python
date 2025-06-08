from playwright.sync_api import expect, Page, BrowserType
from tests.utils.constants import BASE_URL
import pytest
home_title = 'Credit Association'
savings_title = 'Save with us'

@pytest.fixture
def page(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=2000).new_page()
    yield page
    page.close()
    print("now is closed!", flush= True)
    
def test_back_forward_reload(page: Page):
    page.goto(BASE_URL)
    page.goto(f'{BASE_URL}savings.html', timeout= 2000)
    expect(page).to_have_title(savings_title)
    
    page.go_back(timeout=10)
    expect(page).to_have_title(home_title)

    page.go_forward(timeout=2000)
    page.reload()
    expect(page).to_have_title(savings_title)

def test_navigation(page: Page):
    page.goto('', wait_until='load', timeout=100)
    expect(page).to_have_title(home_title)


def test_load_speed_while_navigating(page: Page):
    page.goto('')
    page.goto(f'savings.html', timeout=5000)
    expect(page).to_have_title(savings_title)

def test_page_back_speed(page: Page):
    page.goto(BASE_URL, wait_until='load', timeout = 3000)
    expect(page).to_have_title(home_title)