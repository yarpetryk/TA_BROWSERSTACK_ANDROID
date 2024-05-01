import pytest
from appium import webdriver
from helpers.config_importer import ConfigImporter
from helpers.config_env import config_env

config_importer = ConfigImporter()
config_env = config_env()

@pytest.fixture(scope='function')
def driver():
    locale = str(config_importer.config_locale())
    language = str(config_importer.config_language())
    capabilities = {
        'language': language,
        'locale': locale
    }
    url = "https://hub-cloud.browserstack.com/wd/hub"
    driver = webdriver.Remote(url, capabilities)
    yield driver
    driver.quit()
