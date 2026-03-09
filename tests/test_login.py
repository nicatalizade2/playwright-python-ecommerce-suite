from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
@pytest.mark.login

def test_valid_login(page):
    login = LoginPage(page)
    login.open_url("/")
    login.open_login_modal()
    login.login("Nicat", "retro007")
    login.verify_login_success("Nicat")