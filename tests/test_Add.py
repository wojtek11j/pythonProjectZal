from telnetlib import EC
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup_and_teardown")
class TestAdd:
    def test_add(self):
        self.driver.find_element(By.ID, "dgwt-wcas-search-input-1").send_keys("Klamka Viva")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Szukaj']//*[name()='svg']").click()
        self.driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
        self.driver.find_element(By.XPATH, "//a[@class='button wc-forward']").click()
        assert self.driver.find_element(By.XPATH,"//span[@class='woocommerce-Price-amount amount']").is_displayed()

    def test_addd_chnging_a_product(self):
        self.driver.find_element(By.ID, "dgwt-wcas-search-input-1").send_keys("Klamka Viva")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Szukaj']//*[name()='svg']").click()
        self.driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
        self.driver.find_element(By.XPATH, "//a[@class='button wc-forward']").click()
        self.driver.find_element(By.XPATH, "//button[@class='increase items-count']").click()
        sleep(6)
        self.driver.find_element(By.XPATH, "//button[@name='update_cart']").click()
        sleep(6)
        self.driver.find_element(By.XPATH, "//h1[@class='entry-title']").is_displayed()

    def test_remove(self):
        self.driver.find_element(By.ID, "dgwt-wcas-search-input-1").send_keys("Klamka Viva")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Szukaj']//*[name()='svg']").click()
        self.driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
        self.driver.find_element(By.XPATH, "//a[@class='button wc-forward']").click()
        self.driver.find_element(By.XPATH, "//button[@class='increase items-count']").click()
        sleep(6)
        self.driver.find_element(By.XPATH, "//a[@class='remove']").click()
        sleep(6)
        self.driver.find_element(By.XPATH, "//a[@href='https://windoor.sklep.pl/shop/']").click()

    def test_add_cayt(self):
        self.driver.find_element(By.XPATH, "//span[@class='name-text']").click()
        sleep(6)
        assert self.driver.find_element(By.XPATH, "//h1[@class='entry-title']").is_displayed()
