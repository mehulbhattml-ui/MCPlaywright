import pytest

from tests.utils.browser import launch_browser
from tests.utils.server import FastMCPServer


@pytest.fixture(scope="session")
def fastmcp_server():
    server = FastMCPServer()
    server.start()
    yield
    server.stop()


@pytest.fixture(scope="session")
def browser():
    with launch_browser(headless=True) as browser_instance:
        yield browser_instance
