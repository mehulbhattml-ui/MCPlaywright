from .base_page import BasePage


class RootPage(BasePage):
    def goto(self) -> None:
        super().goto("/")

    def body_text(self) -> str | None:
        return self.text("body")

    def title(self) -> str | None:
        return self.page.title()
