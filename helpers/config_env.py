import os
from dotenv import load_dotenv
from helpers.config_importer import ConfigImporter


def config_env():
    config_importer = ConfigImporter()
    env_path = config_importer.config_env()
    load_dotenv(dotenv_path=env_path)
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    browserstack_username = os.getenv("BROWSERSTACK_USERNAME")
    browserstack_access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    return {
        "login": login,
        "password": password,
        "base_url": base_url,
        "browserstack_username": browserstack_username,
        "browserstack_access_key": browserstack_access_key

    }
