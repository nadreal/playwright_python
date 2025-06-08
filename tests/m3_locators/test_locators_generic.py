from playwright.sync_api import Page, expect

page.goto("http://localhost:8000/")
    page.get_by_role("textbox", name="First name").click()
    page.get_by_role("textbox", name="First name").fill("Stevan")
    page.get_by_role("textbox", name="Last name").click()
    page.get_by_role("textbox", name="Last name").fill("t")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("ss")
    page.get_by_role("textbox", name="Date of birth (optional)").fill("2025-05-01")
    page.get_by_role("checkbox", name="I wish to share how I've").check()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Clear").click()
    page.get_by_role("button", name="Register").click()
    page.get_by_role("button", name="Save input").click()

    # ---------------------
    context.close()
    browser.close()
    
def test_generic_locators(page: Page):
    page.goto('')
