from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage():
    def init(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def shop_login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def add_item_to_card(self):
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item_name in items_to_add:
            item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
            self.driver.find_element(By.XPATH, item_xpath).click()

    def click_to_card(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def fill_user_data(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Иван")
        self.driver.find_element(By.ID, "last-name").send_keys("Петров")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()

    def get_total_sum(self):
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_amount = total_text.split()[-1]  # Извлекаем "$58.29" из текста

        return total_amount