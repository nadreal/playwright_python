from playwright.sync_api import Page
from tests.utils.constants import BASE_URL

def test_fill(page: Page):
    page.goto(BASE_URL)
    page.get_by_label('First name').fill('Zabuci')
    page.get_by_label('Date of Birth').fill('1994-12-20')

def test_click_demo(page: Page):
    page.goto('')
    btn = page.get_by_role('button', name='Register')
    btn.click()
    
    btn.click(click_count=5)
    btn.click(button='right')
    btn.dblclick()
