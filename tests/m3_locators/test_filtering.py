from playwright.sync_api import Page, expect, BrowserType
from tests.utils.constants import BASE_URL
import pytest, logging

@pytest.fixture
def page(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=2000).new_page()
    yield page
    page.close()
    print("now is closed!", flush= True)
    
def test_filtering_demo(page):
    page.goto(f'{BASE_URL}savings.html')
    row = page.get_by_role('row').filter(has_text='Competition')
    print(row.count())
    cell = page.get_by_role('row').filter(has_text='Competition').get_by_role('cell').nth(1)
    print(cell.count())
    print(cell.text_content())
    
    
    
