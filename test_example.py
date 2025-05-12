import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


class TestExample:
    @pytest.fixture
    def driver(self):
        options = ChromeOptions()
        options.set_capability('acceptInsecureCerts', True)
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub",
            desired_capabilities=capabilities,
            options=options)
        driver.maximize_window()
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        yield driver
        driver.quit()

    def test(self, driver):
        assert driver.find_element(By.XPATH, "//button[text()='Вход и регистрация']").is_displayed()
