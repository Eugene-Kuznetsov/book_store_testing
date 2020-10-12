import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
account_btn = driver.find_element_by_css_selector("#menu-item-50 > a")
account_btn.click()
login_email = driver.find_element_by_id("username")
login_email.send_keys("evgeniy.online@mail.ru")
login_password = driver.find_element_by_id("password")
login_password.send_keys("Mylosangeles6259119")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
shop_btn.click()
book_btn = driver.find_element_by_css_selector(".post-169 > a")
book_btn.click()
first_price = driver.find_element_by_css_selector(".price > del > span")
first_price_text = first_price.text
print("Цена товара без скидки: ", first_price_text)
assert "₹600.00" in first_price_text
sale_price = driver.find_element_by_css_selector(".price > ins > span")
sale_price_text = sale_price.text
assert sale_price_text == "₹450.00"
print("Цена товара со скидкой: ", sale_price_text)
time.sleep(20)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a"))).click()
time.sleep(5)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
driver.quit()

