import re
from playwright.sync_api import Playwright, sync_playwright, expect, Page
from pages.cookie_modal import CookieModal

def test_cookie_analytic(page: Page):
    page.goto("https://www.ing.pl/")
    cookie_modal = CookieModal(page)
    cookie_modal.wait_for_modal()
    cookie_modal.accept_analytics()

    cookies = page.context.cookies()
    target_cookie = next((cookie for cookie in cookies if cookie["name"] == "cookiePolicyGDPR"), None)
    assert target_cookie is not None, "Missing cookie element"
    assert target_cookie["value"] == "3", f'Cookie value is {target_cookie["value"]}, expected "3"'
   


