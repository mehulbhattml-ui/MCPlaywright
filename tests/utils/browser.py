from contextlib import contextmanager

from playwright.sync_api import Browser, sync_playwright


@contextmanager
def launch_browser(headless: bool = True):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        try:
            yield browser
        finally:
            browser.close()
