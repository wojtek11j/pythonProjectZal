import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_produkt(self):
        self.driver.find_element(By. XPATH, "//img[@alt='Drzwi WINDOOR – sklep internetowy producenta drzwi i profili WPC']").is_displayed()

