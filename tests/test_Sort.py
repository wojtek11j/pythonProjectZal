from time import sleep

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSort:
    def test_sort_popularity(self):
        self.driver.find_element(By.XPATH, "//a[@class='mega-menu-link'][contains(text(),'Drzwi wewnętrzne')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='orderby']").click()
        self.driver.find_element(By.XPATH, "//option[@value='popularity']").click()
        sleep(3)
        assert self.driver.find_element(By.XPATH, "//h1[@class='page-title']").is_displayed()

    def test_sort_date(self):
        self.driver.find_element(By.XPATH, "//a[@class='mega-menu-link'][contains(text(),'Drzwi wewnętrzne')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='orderby']").click()
        sleep(4)
        self.driver.find_element(By.XPATH, "//option[@value='date']").click()
        sleep(4)
        assert self.driver.find_element(By.XPATH, "//h1[@class='page-title']").is_displayed()
        sleep(4)

    def test_sort_price(self):
        self.driver.find_element(By.XPATH, "//a[@class='mega-menu-link'][contains(text(),'Drzwi wewnętrzne')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='orderby']").click()
        self.driver.find_element(By.XPATH, "//option[@value='price']").click()
        sleep(3)
        assert self.driver.find_element(By.XPATH, "//h1[@class='page-title']").is_displayed()

    def test_sort_price_desc(self):
        self.driver.find_element(By.XPATH, "//a[@class='mega-menu-link'][contains(text(),'Drzwi wewnętrzne')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='orderby']").click()
        self.driver.find_element(By.XPATH, "//option[@value='price-desc']").click()
        sleep(5)
        assert self.driver.find_element(By.XPATH, "//h1[@class='page-title']").is_displayed()
