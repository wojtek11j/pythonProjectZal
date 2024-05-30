import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_produkt(self):
        self.driver.find_element(By.ID, "dgwt-wcas-search-input-1").send_keys("Klamka Viva")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Szukaj']//*[name()='svg']").click()
        assert self.driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").is_displayed()

    def test_search_for_valid_produkt(self):
        self.driver.find_element(By.ID, "dgwt-wcas-search-input-1").send_keys("Okno")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Szukaj']//*[name()='svg']").click()
        expected_text = "Nie znaleziono produktów, których szukasz."
        assert self.driver.find_element(By.XPATH, "//p[@class='woocommerce-info']").text.__eq__(expected_text)
