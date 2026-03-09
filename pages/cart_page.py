from playwright.sync_api import expect
from.base_page import BasePage

class CartPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.btn_place_order = self.page.get_by_role("button", name="Place Order")
        self.btn_purchase = self.page.get_by_role("button", name="Purchase")
        self.btn_confirm_ok = self.page.get_by_role("button", name="OK")

    def open_checkout_modal(self):
        self.btn_place_order.click()
        expect(self.page.get_by_role('heading', name='Place Order')).to_be_visible()

    def fill_order_form(self, name, country, city, card, month, year):
        self.page.locator("#name").fill(name)
        self.page.locator("#country").fill(country)
        self.page.locator("#city").fill(city)
        self.page.locator("#card").fill(card)
        self.page.locator("#month").fill(month)
        self.page.locator("#year").fill(year)

    def complete_purchase(self):
        self.btn_purchase.click()

        success_message = self.page.get_by_text("Thank you for your purchase!")
        expect(success_message).to_be_visible()

        self.btn_confirm_ok.click()
        expect(success_message).not_to_be_visible()