from playwright.sync_api import Page, Response, Request
from tests.utils.constants import BASE_URL
from pprint import pprint

def test_request_response_overview(page: Page):
    response: Response = page.goto(BASE_URL)
    
    print(response.url)
    print(response.status)
    print(response.ok)
    
    pprint(response.all_headers())
    pprint(response.headers_array())
    
    # print('body je:', response.body())
    # print('sta je ovo', response.text())
    
    # print(response.json())

    request: Request = response.request
    print('/nkoja je ovde razlika: ', request.all_headers())
    print(request.method)
    print("DONE!")