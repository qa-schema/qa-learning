import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def driver():
    options = Options()

    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")          # 👈 ДОБАВИТЬ
        options.add_argument("--window-size=1920,1080") # 👈 ДОБАВИТЬ

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()
