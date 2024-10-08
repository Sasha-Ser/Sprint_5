from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import pytest


class TestToConstructor:

    def test_to_constructor_from_cabinet_through_logo_true(self, authorization):
        authorization.find_element(By.XPATH, Locators.header_logo).click()

        assert authorization.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_to_constructor_from_cabinet_through_header_true(self, authorization):
        authorization.find_element(By.XPATH, Locators.header_constructor).click()

        assert authorization.current_url == 'https://stellarburgers.nomoreparties.site/'


