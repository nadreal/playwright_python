import pytest
from playwright.sync_api import expect, Page
from tests.utils.constants import BASE_URL
import requests

@pytest.fixture(scope='module')
def once_per_module(page: Page):
    name = requests.get('https://api.github.com/users/andrejs-ps').json().get('name')

@pytest.fixture(scope='function')
def page(page: Page):
    page.goto(BASE_URL)
    print ('setup')
    yield page
    print ('\ncleanup')   

@pytest.mark.parametrize('name, last_name', [('Bob',' Markovi'),('Familija','Kuridza'),('Georgije','Nikolic')])
def test_single_param_with_bob(page: Page, once_per_module, name: str, last_name: str):
    name_input = page.get_by_label('First name')
    name_input.fill(name)
    expect(name_input).to_have_value(name)
    
    last_name_input = page.get_by_label('Last name')
    last_name_input.fill(last_name)
    expect(last_name_input).to_have_value(last_name)
    print(f'Test1: {once_per_module}')


def test_single_param_with_alexandrina(page: Page, once_per_module):
    name_input = page.get_by_label('First name')
    name_input.fill('Alexandrina')
    expect(name_input).to_have_value('Alexandrina')
    print(f'Test2: {once_per_module}')
    

    # ...


# After: to parameterize
def test_single_param(page: Page):
    name_input = page.get_by_label('First name')
    name_input.fill('')
    expect(name_input).to_have_value('')

    # ...


# After: to parameterize with tuples
def test_two_params(page: Page):
    first_name_input = page.get_by_label('First name')
    first_name_input.fill('')
    expect(first_name_input).to_have_value('')

    last_name_input = page.get_by_label('Last name')
    last_name_input.fill('')
    expect(last_name_input).to_have_value('')
