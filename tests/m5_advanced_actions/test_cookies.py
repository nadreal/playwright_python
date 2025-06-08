from playwright.sync_api import Page, expect, BrowserType
from tests.utils.constants import BASE_URL
import pytest, logging


def test_cookies(page: Page):
    page.goto(BASE_URL)

    print(page.context.cookies())
    
    page.context.add_cookies([{
        'name': 'cookie1',
        'value': '123',
        'url': 'https://playwright.dev/python/'
    }])
    print(page.context.cookies())
    page.context.clear_cookies()
    print("after a clearance: ")
    print(page.context.cookies())