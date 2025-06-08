from playwright.sync_api import expect, Page, BrowserType
from tests.utils.constants import BASE_URL
import pytest
from playwright.sync_api import sync_playwright, expect


home_title = 'Credit Association'
invalid_feedback = 'Please enter a valid email address'
                
@pytest.fixture
def page(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=2000).new_page()
    yield page
    page.close()
        
def test_check_reload(page):
    page.goto(BASE_URL)
    expect(page).to_have_title(home_title)
    
    page.get_by_role('button', name="Register", exact=True).click()
    feedback = page.locator('.invalid-feedback')
    print(f'{feedback} DAKLE DAKLE!!!')
    expect(feedback).to_have_count(3)
    feedback.first.wait_for(state='visible')
    page.reload()
    # expect(feedback).not_to_be_visible()
    expect(feedback).to_have_count(3)
    for message in feedback.all():
        expect(message).not_to_be_visible()
    # expect(feedback).not_to_be_visible()
    
    page.get_by_label('Date of birth').fill('2024-10-10')
    
def test_check_radio(page):
    page.goto(BASE_URL)
    checkbox = page.get_by_role('checkbox')
    textarea = page.locator('#textarea')
    message = 'Jo Jo'
    
    checkbox.check()
    textarea.fill(message)
    # expect(textarea).to_have_value(message)
    expect(textarea).to_contain_text(message)
    
def test_check_the_check(page: Page):
    page.goto(BASE_URL)
    checkbox = page.get_by_role('checkbox')
    checkbox.check()
    textarea = page.locator('#textarea')
    message = "Gde si koko?"
    textarea.type(message)
    
    expect(textarea).to_have_value(message)