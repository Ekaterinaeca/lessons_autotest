from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        """Open calculator page."""
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)

    def set_delay(self, delay):
        """Set calculation delay."""
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_buttons(self):
        """Click calculator buttons for 7 + 8 = operation."""
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            self.driver.find_element(
                By.XPATH, f"//span[text()='{button}']"
            ).click()

    def get_result(self):
        """Get calculation result."""
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text