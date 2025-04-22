from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # 🧩 Auto-manage ChromeDriver
import time
import re

def scrape_amazon_laptops():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Auto-install and set up ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.amazon.in/s?k=laptops")
    time.sleep(3)

    results = []
    products = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")

    for product in products[:20]:
        try:
            title = product.find_element(By.CSS_SELECTOR, "h2 span").text
            price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            rating_element = product.find_element(By.CSS_SELECTOR, ".a-icon-star-small span.a-icon-alt")
            rating = rating_element.get_attribute("innerHTML").split()[0]
            results.append({
                "title": title,
                "price": float(price.replace(',', '')),
                "rating": float(rating)
            })
        except:
            continue

    driver.quit()
    return results
