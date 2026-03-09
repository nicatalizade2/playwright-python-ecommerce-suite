from .base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    def add_product_to_cart(self, product_name:str):
        self.page.get_by_role('link', name=product_name).click()

        self.page.once("dialog", lambda d: d.accept())

        self.page.get_by_role('link', name="Add to cart").click()

    def navigate_to_cart(self):
        self.nav_cart.click()
        expect(self.page.get_by_role("heading", name="Products")).to_be_visible()