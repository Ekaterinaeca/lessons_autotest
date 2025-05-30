import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def init(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        # 2. Установка задержки 45 секунд
    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

        # 3. Нажатие кнопок 7 + 8 =
    def click_buttons(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Ожидание результата с явным ожиданием
    def get_result(self, delay):
        wait = WebDriverWait(self.driver, delay)  # На 1 секунду больше чем задержка
        result = wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"),
            "15"
        ))

        # 5. Проверка результата
        result_text = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result_text