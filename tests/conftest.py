from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import pytest

@pytest.fixture(scope='function')
def authorization(setup_driver):

    setup_driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
    setup_driver.find_element(By.XPATH, Locators.autorization_email).send_keys('sasha_sergeev_14@yandex.ru')
    setup_driver.find_element(By.XPATH, Locators.autorization_password).send_keys('123456')
    setup_driver.find_element(By.XPATH, Locators.autorization_button).click()
    WebDriverWait(setup_driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, Locators.text_on_main_page)))
    setup_driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
    WebDriverWait(setup_driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, Locators.text_in_cabinet)))
    return setup_driver

@pytest.fixture(scope='function')
def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


