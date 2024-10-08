import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from locators import Locators

class TestRegistration:
    def test_registration_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        #регистрация
        driver.find_element(By.XPATH, Locators.registration_name).send_keys('Саша')
        (driver.find_element(By.XPATH, Locators.registration_email).send_keys
         (f'{random.randint(1,999)}_1sasha_sergeev_14@yandex.ru'))
        driver.find_element(By.XPATH, Locators.registration_password).send_keys('123456')
        driver.find_element(By.XPATH, Locators.registration_button).click()
        WebDriverWait(driver, 15).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert 'https://stellarburgers.nomoreparties.site/login' == driver.current_url
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
