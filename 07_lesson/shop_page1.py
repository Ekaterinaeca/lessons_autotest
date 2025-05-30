from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Open the shop website."""
        self.driver.get("https://www.saucedemo.com/")

    def shop_login(self):
        """Login to the shop."""
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def add_item_to_card(self):
        """Add items to shopping cart."""
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item_name in items_to_add:
            item_xpath = (
                f"//div[text()='{item_name}']/"
                "ancestor::div[@class='inventory_item']//button"
            )
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, item_xpath))
            ).click()

    def click_to_card(self):
        """Open shopping cart."""
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    def checkout(self):
        """Proceed to checkout."""
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def fill_user_data(self):
        """Fill user information for checkout."""
        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys("Иван")
        
        self.driver.find_element(By.ID, "last-name").send_keys("Петров")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()

    def get_total_sum(self):
        """Get total order amount."""
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.split()[-1]
