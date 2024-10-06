import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

@pytest.mark.usefixtures('registration_check_out')
class TestEnterInAccount:

    def test_enter_through_personal_cabinet_button_true(self, registration_check_out):
        driver = registration_check_out
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.autorization_personal_cabinet_button).click()

    def test_enter_through_enter_in_account_button_true(self, registration_check_out):
        driver = registration_check_out
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.autorization_enter_in_account_button).click()

    def test_enter_through_registration_page_true(self, registration_check_out):
        driver = registration_check_out
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH, Locators.enter_on_registration_page).click()

    def test_enter_through_forgot_page_true(self, registration_check_out):
        driver = registration_check_out
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(By.XPATH, Locators.enter_on_registration_page).click()
