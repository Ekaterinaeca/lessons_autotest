import pytest
import allure
from selenium import webdriver
from shop_page import ShopPage


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Тесты магазина")
@allure.severity(allure.severity_level.BLOCKER)
class TestShop:
    """Класс с тестами для магазина."""

    @allure.title("Тест процесса оформления заказа")
    @allure.description("Проверка полного цикла оформления заказа в магазине")
    def test_shop_page(self, driver):
        """Тест процесса оформления заказа."""
        shop_page = ShopPage(driver)
        
        with allure.step("Открытие и авторизация"):
            shop_page.open()
            shop_page.shop_login()
        
        with allure.step("Добавление товаров в корзину"):
            shop_page.add_item_to_card()
            shop_page.click_to_card()
        
        with allure.step("Оформление заказа"):
            shop_page.checkout()
            shop_page.fill_user_data()
        
        with allure.step("Проверка итоговой суммы"):
            assert shop_page.get_total_sum() == "$58.29", "Ожидаемая сумма $58.29, получена другая сумма"