from pages.home_page import HomePage
import pytest
from playwright.sync_api import expect

@pytest.mark.ui
@pytest.mark.cart

def test_add_product_to_cart(page):
    home = HomePage(page)
    home.open_url("/")
    home.add_product_to_cart("Samsung galaxy s6")
    home.navigate_to_cart()
    expect(page.get_by_role("cell", name="Samsung galaxy s6")).to_be_visible()