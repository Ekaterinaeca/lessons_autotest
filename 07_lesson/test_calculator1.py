import pytest
from selenium import webdriver
from calculator_page1 import CalculatorPage


@pytest.fixture
def driver():
    """Fixture to initialize and quit browser."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_page(driver):
    """Test calculator with delay."""
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.set_delay("20")
    calc_page.click_buttons()
    assert (
        calc_page.get_result() == "15"
    ), "Expected result '15', got different value"
