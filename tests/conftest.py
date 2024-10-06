from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import pytest

@pytest.fixture(scope='class')
def authorization():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
    driver.find_element(By.XPATH, Locators.autorization_email).send_keys('sasha_sergeev_14@yandex.ru')
    driver.find_element(By.XPATH, Locators.autorization_password).send_keys('123456')
    driver.find_element(By.XPATH, Locators.autorization_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, Locators.text_on_main_page)))
    driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, Locators.text_in_cabinet)))
    return driver

@pytest.fixture(scope='class')
def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver

@pytest.fixture(scope='class')
def registration_check_out():
    driver = webdriver.Chrome()
    yield driver
    driver.find_element(By.XPATH, Locators.autorization_email).send_keys('sasha_sergeev_14@yandex.ru')
    driver.find_element(By.XPATH, Locators.autorization_password).send_keys('123456')
    driver.find_element(By.XPATH, Locators.autorization_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, Locators.text_on_main_page)))
    driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, Locators.text_in_cabinet)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    driver.quit()
