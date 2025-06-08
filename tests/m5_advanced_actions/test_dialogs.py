from playwright.sync_api import expect, Page
from tests.utils.constants import BASE_URL
import time
name = 'Jovanka'


# Default handling is to dismiss
def test_dialog_default_handling(page: Page):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    expect(name_input).to_have_value(name)

    page.get_by_role('button', name='Clear').click()
    expect(name_input).to_have_value(name)


def test_dialog_ok_or_dismiss(page: Page):
    # You can use page.once aswell 
    page.on('dialog', lambda popup: popup.accept())
    page.on('console', lambda msg: print(msg.text))
    page.on('pageerror', lambda msg: print(msg))
    page.goto(BASE_URL)
    
    time.sleep(4)
    input_name = page.get_by_label('First name')
    input_name.fill(name)

    page.get_by_role('button', name='Register').click()
   
   # expect(input_name).to_have_value('')
