from typing import Optional

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, host: str = "http://localhost:8001"):
        self.page = page
        self.host = host

    def goto(self, path: str = "/") -> None:
        self.page.goto(f"{self.host}{path}")

    def text(self, selector: str) -> Optional[str]:
        return self.page.text_content(selector)
