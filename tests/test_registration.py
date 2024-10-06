import random

from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import Locators

@pytest.mark.usefixtures('setup_driver')
class TestRegistration:

    def test_registration_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        #регистрация
        driver.find_element(By.XPATH, Locators.registration_name).send_keys('Саша')
        (driver.find_element(By.XPATH, Locators.registration_email).send_keys
         (f'{random.randint(1,999)}_sasha_sergeev_14@yandex.ru'))
        driver.find_element(By.XPATH, Locators.registration_password).send_keys('123456')
        driver.find_element(By.XPATH, Locators.registration_button).click()

        driver.quit()

    def test_registration_5_symbol_in_password_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # регистрация
        driver.find_element(By.XPATH, Locators.registration_name).send_keys('Саша')
        driver.find_element(By.XPATH, Locators.registration_email).send_keys("0_sasha_sergeev_14@yandex.ru")
        driver.find_element(By.XPATH, Locators.registration_password).send_keys(f'{random.randint(1, 99999)}')
        driver.find_element(By.XPATH, Locators.registration_button).click()

        invalid_password_text = driver.find_element(By.XPATH, Locators.registration_invalid_password).text
        assert invalid_password_text == 'Некорректный пароль'

        driver.quit()



