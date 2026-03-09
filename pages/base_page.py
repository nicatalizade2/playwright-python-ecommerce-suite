import re
from playwright.sync_api import Page,expect
class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.nav_home = page.get_by_role('link', name="Home")
        self.nav_cart = page.get_by_role('link', name="Cart", exact=True)
        self.nav_login = page.get_by_role('link', name="Log in")
        self.welcome_user = page.locator("#nameofuser")

    def open_url(self, path: str = "/"):
        self.page.goto(path)

    def verify_url_contains(self, pattern: str):
        expect(self.page).to_have_url(re.compile(pattern))



