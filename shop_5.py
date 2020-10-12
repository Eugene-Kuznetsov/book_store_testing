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
driver.execute_script("window.scrollBy(0,300);")
html5_btn = driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a[2]")
html5_btn.click()
time.sleep(5)
jsdata_btn = driver.find_element_by_xpath("//*[@id='content']/ul/li[5]/a[2]")
jsdata_btn.click()
time.sleep(5)
basket_content_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_content_btn.click()
time.sleep(5)
item_remove = driver.find_element_by_class_name("remove")
item_remove.click()
time.sleep(5)
undo_btn = driver.find_element_by_css_selector(".woocommerce-message > a")
undo_btn.click()
time.sleep(5)
quantity_btn = driver.find_element_by_css_selector(".quantity > input")
quantity_btn.clear()
quantity_btn.send_keys("3")
update_btn = driver.find_element_by_name("update_cart")
update_btn.click()
time.sleep(5)
jsdata_value = driver.find_element_by_css_selector(".quantity > input")
jsdata_value_text = jsdata_value.get_attribute("value")
assert jsdata_value_text == "3"
print("Количество товара JS Data Structures and Algorithm: ", jsdata_value_text)
time.sleep(5)
coupon_btn = driver.find_element_by_name("apply_coupon")
coupon_btn.click()
time.sleep(10)
enter_coupon = driver.find_element_by_css_selector(".woocommerce-error > li")
enter_coupon_text = enter_coupon.text
assert enter_coupon_text == "Please enter a coupon code."
print("Надпись после нажатия кнопки купона: ", enter_coupon_text)

driver.quit()