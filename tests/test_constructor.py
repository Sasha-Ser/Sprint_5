from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
import pytest

@pytest.mark.usefixtures('setup_driver')
class TestConstructor:

    def test_go_to_the_sauce_section(self, setup_driver):
        driver = setup_driver
        driver.find_element(By.XPATH, Locators.constructor_section_sauce).click()

        assert 'current' in driver.find_element(By.XPATH, Locators.constructor_section_sauce).get_attribute('class')

        driver.quit()

    def test_go_to_the_filling_section(self, setup_driver):
        driver = setup_driver
        driver.find_element(By.XPATH, Locators.constructor_section_filling).click()

        assert 'current' in driver.find_element(By.XPATH, Locators.constructor_section_filling).get_attribute('class')

        driver.quit()

    def test_go_to_the_bread_section(self, setup_driver):
        driver = setup_driver
        driver.find_element(By.XPATH, Locators.constructor_section_filling).click()
        driver.find_element(By.XPATH, Locators.constructor_section_breads).click()

        assert 'current' in driver.find_element(By.XPATH, Locators.constructor_section_breads).get_attribute('class')

        driver.quit()
