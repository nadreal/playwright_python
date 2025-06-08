from playwright.sync_api import Page
from tests.utils.constants import BASE_URL
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import time


def test_multiple_matches_fails(page: Page):
    page.goto('')


def test_multiple_matches_first_last_nth(page: Page):
    page.goto(BASE_URL, slow_mo=1000)
    feedback = page.locator('.invalid-feedback')
    expect(feedback).to_have_count(3)
    page.get_by_role('button', name ='Register', exact = True).click()
    for message in feedback.all():
        expect(message).to_be_visible()

def test_multiple_matches_count_or_iterate(page):
    page.goto('')
    page.get_by_role('button', name='Register').click()

def test_multiple_match(page: Page):
    page.goto(BASE_URL)
    #Unable to do click action on multiply locators found
    #page.get_by_role('link').click()
    buttons = page.get_by_role('link')
    print(buttons.first.text_content())
    print(buttons.nth(1).text_content())
    
def  test_mulitple_matches_count(page: Page):
    page.goto(BASE_URL)
    time.sleep(5)
    #page.get_by_role('button', name ='Register').click()
    feedback = page.locator('.invalid-feedback')
    #expect(feedback).to_have_count(3)
    
    for message in feedback.all():
        expect(message).to_be_visible()
        