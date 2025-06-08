from playwright.sync_api import expect, Page, BrowserType
from tests.utils.constants import BASE_URL
import pytest
                
@pytest.fixture
def page(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=2000).new_page()
    yield page
    page.close()
    
def test_select(page):
    page.goto(f'{BASE_URL}savings.html')
    

    deposit = page.get_by_test_id('deposit')
    period = page.get_by_test_id('period')
    result = page.get_by_test_id('result')

    deposit.fill('100')
    period.select_option('6 Months')
    expect(result).to_have_text('After 6 Months you will earn $2.00 on your deposit')