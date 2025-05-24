from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 15).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 4
    )

    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")

        print(third_image_src)
    else:
        print("Не найдено 3 картинок на странице")

finally:
    driver.quit()