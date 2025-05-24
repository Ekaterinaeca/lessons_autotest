import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    try:
        # 1. Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. Установка задержки 45 секунд
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажатие кнопок 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Ожидание результата с явным ожиданием
        WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

        # 5. Проверка результата
        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result_text == "15", f"Ожидался результат 15, получено {result_text}"

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()