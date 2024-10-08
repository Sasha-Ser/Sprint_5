import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestEnterInAccount:

    def test_enter_through_personal_cabinet_button_true(self, setup_driver):
        driver = setup_driver

        driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
        driver.find_element(By.XPATH, Locators.autorization_email).send_keys('sasha_sergeev_14@yandex.ru')
        driver.find_element(By.XPATH, Locators.autorization_password).send_keys('123456')
        driver.find_element(By.XPATH, Locators.autorization_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_on_main_page)))
        driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_in_cabinet)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'


    def test_enter_through_enter_in_account_button_true(self, setup_driver):
        driver = setup_driver

        driver.find_element(By.XPATH, Locators.autorization_enter_in_account_button).click()
        driver.find_element(By.XPATH, Locators.autorization_email).send_keys('sasha_sergeev_14@yandex.ru')
        driver.find_element(By.XPATH, Locators.autorization_password).send_keys('123456')
        driver.find_element(By.XPATH, Locators.autorization_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_on_main_page)))
        driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_in_cabinet)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'


    def test_enter_through_registration_page_true(self, setup_driver):
        driver = setup_driver

        driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
        driver.find_element(By.XPATH, Locators.enter_link_registration).click()
        driver.find_element(By.XPATH, Locators.enter_on_registration_page).click()
        driver.find_element(By.XPATH, Locators.autorization_email).send_keys('sasha_sergeev_14@yandex.ru')
        driver.find_element(By.XPATH, Locators.autorization_password).send_keys('123456')
        driver.find_element(By.XPATH, Locators.autorization_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_on_main_page)))
        driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_in_cabinet)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'


    def test_enter_through_forgot_page_true(self, setup_driver):
        driver = setup_driver

        driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
        driver.find_element(By.XPATH, Locators.enter_forgot_password).click()
        driver.find_element(By.XPATH, Locators.enter_on_registration_page).click()
        driver.find_element(By.XPATH, Locators.autorization_email).send_keys('sasha_sergeev_14@yandex.ru')
        driver.find_element(By.XPATH, Locators.autorization_password).send_keys('123456')
        driver.find_element(By.XPATH, Locators.autorization_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_on_main_page)))
        driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_in_cabinet)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'