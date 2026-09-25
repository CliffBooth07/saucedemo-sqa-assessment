import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):
    options = Options()
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-notifications")

    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(30)
    yield browser

    if request.node.rep_call and request.node.rep_call.failed:
        screenshot_dir = Path("artifacts")
        screenshot_dir.mkdir(exist_ok=True)
        browser.save_screenshot(str(screenshot_dir / f"{request.node.name}.png"))
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
