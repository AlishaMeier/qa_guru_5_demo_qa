import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def window_configurate_chrome():
    browser.config.window_width = 1200
    browser.config.window_height = 900
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.hold_browser_open = True
    browser.config.timeout = 10
    yield
