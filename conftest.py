import pytest

@pytest.fixture(autouse=True)
def clear_cookies_before_each(page):
    page.context.clear_cookies()
