import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=["chrome", "firefox"])
def fixtureSetup(request):
    driver = None
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("-headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    if request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("-headless")
        firefox_options.add_argument("-no-sandbox")
        firefox_options.add_argument("-window-size=1920,1080")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    return driver