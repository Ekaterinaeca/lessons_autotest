from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sauce_demo_purchase():
    driver = webdriver.Firefox()  # Изменено здесь
    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item_name in items_to_add:
            item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
            driver.find_element(By.XPATH, item_xpath).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_amount = total_text.split()[-1]  # Извлекаем "$58.29" из текста

        assert total_amount == "$58.29", f"Ожидалась сумма $58.29, получено {total_amount}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_sauce_demo_purchase()