from pprint import pprint
from tests.utils.constants import BASE_URL
from playwright.sync_api import expect, Page, APIResponse, Playwright, APIRequestContext, Response


def test_api_request_response(page: Page):
    response: Response = page.goto(BASE_URL)
    api_ctx: APIRequestContext = page.request
    
    api_response: APIResponse = api_ctx.get('https://api.github.com/')
    
    print (api_response.ok)
    print(api_response.status)
    pprint(api_response.headers_array)
    pprint(api_response.json())
    
    #expect(response).to_be_ok() NO!!!
    expect(api_response).to_be_ok()

def test_api_request_context(playwright: Playwright):
    pass
