import pytest
import yaml
from utils.logger import get_logger
from api.api_client import APIClient
from db.db_client import DBClient

logger = get_logger()

@pytest.fixture(scope="session")
def config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def db():
    client = DBClient()
    client.connect()
    client.execute_query("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            product_name VARCHAR(255),
            customer_name VARCHAR(255),
            status VARCHAR(50)
        )
    """)
    yield client
    client.close()
# @pytest.fixture(scope="session", autouse=True)
# def db_setup():
#     client = DBClient()
#     client.connect()
#     client.execute_query("""
#         CREATE TABLE IF NOT EXISTS orders (
#             id SERIAL PRIMARY KEY,
#             product_name VARCHAR(255),
#             customer_name VARCHAR(255),
#             status VARCHAR(50)
#         );
#     """)
#     yield client
#     client.close()
#
#

@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]

# @pytest.fixture
# def browser_context_args(base_url):
#     return {
#         "base_url": base_url
#     }
@pytest.fixture(scope="session")
def test_settings(config):
    return {
        "base_url" : config["base_url"],
        "viewport": {"width": 1280, "height": 720}
    }

@pytest.fixture(autouse=True)
def log_test_lifecycle(request):
    logger.info(f"--- Starting Test: {request.node.name} ---")
    yield
    logger.info(f"--- Finished Test: {request.node.name} ---")


@pytest.fixture(scope="session")
def api_context(playwright, config):
    context = playwright.request.new_context(base_url=config["api_base_url"])
    yield context
    context.dispose()

@pytest.fixture
def api_client(api_context, config):
    return APIClient(api_context, config["api_base_url"])



