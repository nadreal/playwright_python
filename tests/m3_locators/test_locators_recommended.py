from playwright.sync_api import Page, expect, BrowserType
from tests.utils.constants import BASE_URL
import pytest, logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@pytest.fixture
def page(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=2000).new_page()
    yield page
    page.close()
    logging.info('This is an info-level log message.')
    
    logger.debug("This is a debug message") 
    print("now is closed!", flush= True)
    

def test_recommended_locators(page):    
    page.goto(BASE_URL)
    print("test")
    first_name = page.get_by_label('First name')
    first_name.fill('Stevan')
    first_name.clear()
    
    logger.debug("This is a debug message") 
    page.get_by_label('First name').fill('Jovanka')
    logging.info('This is an info-lsage.')
    page.get_by_label('Last Name').fill('Milovac')
    page.locator('#email').fill("test")
    page.query_selector('#email').fill("test@test.com")
   
    

    page.locator('#email').fill("test")
    
    cell = page.get_by_role('row').filter(has_text="Competition").get_by_role('cell').nth(1)
    print(cell.text_content, flush= True)
    warning = page.get_by_text('Please enter a valid email address')
    expect (warning).not_to_be_visible()
