from tests.pages.root_page import RootPage


def test_playwright_loads_root_page(browser, fastmcp_server):
    page = browser.new_page()
    root_page = RootPage(page)
    root_page.goto()

    assert "FastMCP example server" in root_page.body_text()
    page.close()
