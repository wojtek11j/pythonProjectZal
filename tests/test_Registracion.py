import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegistration:
    def test_register_empty_field(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Rejestracja']").click()
        self.driver.find_element(By.ID, "reg_username").send_keys("")
        self.driver.find_element(By.ID, "reg_email").send_keys("wjj1@o2.pl")
        self.driver.find_element(By.ID, "reg_password").send_keys("haslo12345!")
        self.driver.find_element(By.XPATH, "//button[@name='register']").click()  # Dodaj click()
        self.heading_text_error = "Błąd: Konto z Twoim adresem e-mail jest już zarejestrowane. Zaloguj się."
        error_message = self.driver.find_element(By.XPATH, "//div[@class='inner_page']//li[1]").text
        assert error_message == self.heading_text_error

    def test_register_without_email(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Rejestracja']").click()
        self.driver.find_element(By.ID, "reg_username").send_keys("Wojtek")
        self.driver.find_element(By.ID, "reg_email").send_keys("")
        self.driver.find_element(By.ID, "reg_password").send_keys("haslo12345!")
        self.driver.find_element(By.XPATH, "//button[@name='register']").click()  # Dodaj click()
        self.heading_text_error = "Błąd: Proszę podać poprawny adres e-mail."
        error_message = self.driver.find_element(By.XPATH, "//div[@class='inner_page']//li[1]").text
        assert error_message == self.heading_text_error

    def test_register_no_data(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Rejestracja']").click()
        self.driver.find_element(By.ID, "reg_username").send_keys("")
        self.driver.find_element(By.ID, "reg_email").send_keys("")
        self.driver.find_element(By.ID, "reg_password").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@name='register']").click()  # Dodaj click()
        heading_text_error = "Błąd: Proszę podać poprawny adres e-mail."
        error_message = self.driver.find_element(By.XPATH, "//div[@class='inner_page']//li[1]").text
        assert error_message == heading_text_error