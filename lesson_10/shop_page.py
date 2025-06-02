from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    """Класс для работы со страницей магазина."""

    def __init__(self, driver):
        """Инициализация страницы магазина.
        
        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """Открытие страницы магазина."""
        self.driver.get("https://www.saucedemo.com/")

    def shop_login(self) -> None:
        """Авторизация в магазине."""
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    def add_item_to_card(self) -> None:
        """Добавление товаров в корзину."""
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

    def click_to_card(self) -> None:
        """Открытие корзины."""
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    def checkout(self) -> None:
        """Оформление заказа."""
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def fill_user_data(self) -> None:
        """Заполнение данных пользователя."""
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Иван")
        self.wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Петров")
        self.wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys("123456")
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def get_total_sum(self) -> str:
        """Получение итоговой суммы заказа.
        
        Returns:
            str: Итоговая сумма
        """
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.split()[-1]