import pytest
from playwright.sync_api import Page


class TestThing:
    @pytest.mark.skip_browser('firefox')
    def test_one(self, page: Page):
        pass
    @pytest.mark.only_browser('firefox')
    def test_two(self, page: Page):
        pass

    @pytest.mark.browser_context_args(locale='es_ES')
    def test_three(self, page: Page):
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone") == "Europe/Madrid"
        assert page.evaluate("window.navigator.languages") == ["es-ES"]

    def test_four(self, page: Page):
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone") == "Europe/Madrid"
        assert page.evaluate("window.navigator.languages") == ["es-ES"]
