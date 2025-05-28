import pytest
from selenium import webdriver
from calculator_page1 import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_page(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.set_delay("20")
    calc_page.click_buttons()
    assert calc_page.get_result("26") == "15"
