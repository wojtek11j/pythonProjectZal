import pytest
from selenium import webdriver


@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://windoor.sklep.pl/")
    request.cls.driver = driver
    yield
    driver.quit()
