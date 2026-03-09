import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.regression
@pytest.mark.cart

def test_checkout(page):
    home = HomePage(page)
    cart = CartPage(page)

    home.open_url("/")
    home.add_product_to_cart("Samsung galaxy s6")

    home.navigate_to_cart()

    cart.open_checkout_modal()
    cart.fill_order_form( name="Nicat",
        country="Poland",
        city="Warsaw",
        card="1111-2222-3333-4444",
        month="05",
        year="2026")

    cart.complete_purchase()