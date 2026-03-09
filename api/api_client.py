from playwright.sync_api import APIRequestContext

class APIClient:
    def __init__(self, api_request_context: APIRequestContext, base_url: str):
        self.api_context = api_request_context
        self.base_url = base_url

    def get_entries(self):
        response = self.api_context.get(f"{self.base_url}/entries")
        return response

    def check_status(self, response):
        assert response.ok, f"API Request failed with status {response.status}"

