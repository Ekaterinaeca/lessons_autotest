from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver):
        """Инициализация страницы калькулятора.
        
        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self) -> None:
        """Открытие страницы калькулятора."""
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)

    def set_delay(self, delay: str) -> None:
        """Установка задержки вычислений.
        
        Args:
            delay: Значение задержки в виде строки
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_buttons(self) -> None:
        """Нажатие кнопок калькулятора для операции 7 + 8 =."""
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            self.driver.find_element(
                By.XPATH, f"//span[text()='{button}']"
            ).click()

    def get_result(self) -> str:
        """Получение результата вычислений.
        
        Returns:
            str: Текст результата на экране калькулятора
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text