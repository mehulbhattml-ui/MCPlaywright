import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from tests.pages.root_page import RootPage

scenarios("../features/root.feature")


@pytest.fixture
def root_context():
    return {}


@given("the FastMCP server is running")
def root_server(fastmcp_server):
    return fastmcp_server


@when("I open the root page")
def open_root_page(browser, root_context):
    page = browser.new_page()
    root_page = RootPage(page)
    root_page.goto()
    root_context["page"] = page
    root_context["root_page"] = root_page


@then(parsers.parse('I should see "{text}" in the page body'))
def assert_body_contains(root_context, text: str):
    assert text in root_context["root_page"].body_text()
    root_context["page"].close()
