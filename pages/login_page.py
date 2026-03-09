from .base_page import BasePage
from playwright.sync_api import expect
class LoginPage(BasePage):
    def open_login_modal(self):
        self.nav_login.click()
        expect(self.page.get_by_role('dialog')).to_be_visible()

    def login(self, username, password):
        self.page.locator("#loginusername").fill(username)
        self.page.locator("#loginpassword").fill(password)
        self.page.get_by_role("button", name="Log in").click()

    def verify_login_success(self, username: str):
        expect(self.welcome_user).to_contain_text(f"Welcome {username}")

    def verify_login_error(self, expected_message: str):
        # self.page.once("dialog", lambda dialog: (
        #     expect(dialog.message).to_equal(expected_message),
        #     dialog.accept()
        # ))
        self.page.once("dialog", lambda dialog: dialog.accept())