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
basket_content_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_content_btn.click()
time.sleep(5)

checkout_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".alt.wc-forward")))
checkout_btn.click()
time.sleep(5)

firstname = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
firstname.send_keys("E")
lastname = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_last_name")))
lastname.send_keys("K")
email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_email")))
email.send_keys("evgeniy.online@mail.ru")
phone = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_phone")))
phone.send_keys("1235645")

country = driver.find_element_by_class_name("select2-arrow").click()
type = driver.find_element_by_class_name("select2-input").send_keys("Russia")
russia = driver.find_element_by_class_name("select2-match").click()
address = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_address_1")))
address.send_keys("New Street")
city = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_city")))
city.send_keys("Moscow")
state = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_state")))
state.send_keys("-")
postcode = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_postcode")))
postcode.send_keys("111111")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(5)

payments = driver.find_element_by_id("payment_method_cheque").click()
place_order = driver.find_element_by_id("place_order").click()
time.sleep(5)
order_status = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received")))
order_status_text = order_status.text
assert order_status_text == "Thank you. Your order has been received."
print("Order Status: ", order_status_text)
payment_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-35']/div/div[1]/table/tfoot/tr[3]/td")))
payment_method_text = payment_method.text
assert payment_method_text == "Check Payments"
print("Payment Method: ", payment_method_text)
time.sleep(5)

driver.quit()