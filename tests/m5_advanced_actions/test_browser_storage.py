from pprint import pprint

from playwright.sync_api import expect, Page
from tests.utils.constants import BASE_URL

name = 'Sofia'


def test_storage_ui_perspective(page: Page):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    page.reload()
    expect(name_input).to_have_value('')

    name_input.fill(name)
    page.get_by_role('button', name='Save Input').click()
    
    storage: StorageState = page.context.storage_state()
    
    print(storage['cookies'])
    print(storage['origins'][0]['localStorage'])
    
    page.reload()
    expect(name_input).to_have_value(name)


def test_local_storage(page: Page):
    page.goto('')
    page.get_by_label('First name').fill(name)
    page.get_by_role('button', name='Save Input').click()


def test_session_storage(page: Page):
    page.goto(BASE_URL)
    page.evaluate("localStorage.setItem('token', 'abc123')")
    
    name_input = page.get_by_label('First name')
    name_input.fill(name)
   
    page.get_by_role('button', name='Save Input').click()   
   
  
    storage = page.context.storage_state()
    assert 'origins' in storage

def test_javascript_and_storage(page: Page):
    page.goto(BASE_URL)
    
    name_input = page.get_by_label('First name')
    name_input.fill(name)
    page.get_by_role('button',name='Save Input').click()
    
    storage: dict = page.evaluate('() => window.localStorage') 
    print(storage)
    
    page.evaluate('()=> window.localStorage.clear()')
    #page.get_by_role('button',name='Save Input').click()
    page.reload()
    
    expect(name_input).to_have_value('')
    
    page.evaluate('() => window.localStorage.setItem("firstName", "Jovanka")')
    page.reload()
    expect (name_input).to_have_value('Jovanka')
    