import pytest
from api.api_client import APIClient

def test_verify_products(api_client):
    response = api_client.get_entries()
    api_client.check_status(response)

    data = response.json()
    assert len(data['Items']) > 0
    print(f"Total products found: {len(data['Items'])}")