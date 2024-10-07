from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import pytest

class TestEnterInCabinet:
    @pytest.mark.usefixtures('setup_driver', 'authorization')
    def test_enter_cabinet_true(self, setup_driver, authorization):
        assert authorization.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
