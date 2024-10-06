from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import pytest

@pytest.mark.usefixtures('authorization')
class TestLogout:

    def test_logout_through_button_in_cabinet_true(self, authorization):
        authorization.find_element(By.XPATH, Locators.button_logout).click()
        WebDriverWait(authorization, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.text_in_log_in)))

        assert authorization.current_url == 'https://stellarburgers.nomoreparties.site/login'
        authorization.quit()