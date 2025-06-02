import pytest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Тесты калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Класс с тестами для калькулятора."""

    @allure.title("Тест калькулятора с задержкой")
    @allure.description("Проверка работы калькулятора с установленной задержкой")
    def test_calculator_page(self, driver):
        """Тест калькулятора с задержкой."""
        calc_page = CalculatorPage(driver)
        
        with allure.step("Открытие страницы калькулятора"):
            calc_page.open()
        
        with allure.step("Установка задержки вычислений"):
            calc_page.set_delay("4")
        
        with allure.step("Выполнение операции 7 + 8"):
            calc_page.click_buttons()
        
        with allure.step("Проверка результата"):
            assert calc_page.get_result() == "15", "Ожидаемый результат '15', получено другое значение"