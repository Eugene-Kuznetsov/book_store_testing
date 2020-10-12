import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
shop_btn.click()
basket_btn = driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a[2]")
basket_btn.click()

item = driver.find_element_by_class_name("cartcontents")
item_text = item.text
assert "1 Item" in item_text
print("Количество товара в корзине: ", item_text)

price = driver.find_element_by_class_name("amount")
price_text = price.text
assert price_text == "₹180.00"
print("Цена товара: ", price_text)

basket_content_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_content_btn.click()

subtotal = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-subtotal > td > span")))
subtotal_text = subtotal.text
assert subtotal_text == "₹180.00"
print("Subtotal price: ", subtotal_text)
total = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-total > td > strong > span")))
total_text = total.text
assert total_text == "₹189.00"
print("Total price: ", total_text)

driver.quit()

