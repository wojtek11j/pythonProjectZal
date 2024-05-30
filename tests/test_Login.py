import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_emai_and_invalid_password(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Logowanie']").click()
        self.driver.find_element(By.ID, "username").send_keys("wefregrgrg@o2.pl")
        self.driver.find_element(By.ID, "password").send_keys("haslo12345!")
        self.driver.find_element(By.NAME, 'login').click()
        assert self.driver.find_element(By.XPATH, "//li[contains(text(),'Nieznany adres e-mail. Proszę sprawdzić ponownie l')]").is_displayed()

    def test_login_with_invalid_emai_and_valid_password(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Logowanie']").click()
        self.driver.find_element(By.ID, "username").send_keys("wjj1@o2.pl")
        self.driver.find_element(By.ID, "password").send_keys("22334")
        self.driver.find_element(By.NAME, 'login').click()
        assert self.driver.find_element(By.XPATH, "//strong[contains(text(),'Błąd:')]").is_displayed()


    def test_Login_without_providing_any_data(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Logowanie']").click()
        self.driver.find_element(By.ID, "username").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.NAME, 'login').click()
        assert self.driver.find_element(By.XPATH,"//div[@class='inner_page']//li[1]").is_displayed()


    def test_log_in_correct_details(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Logowanie']").click()
        self.driver.find_element(By.ID, "username").send_keys("wjj1@o2.pl")
        self.driver.find_element(By.ID, "password").send_keys("haslo12345!")
        self.driver.find_element(By.NAME, 'login').click()
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'Witaj')]").is_displayed()
