import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

account_btn = driver.find_element_by_css_selector("#menu-item-50 > a")
account_btn.click()
email = driver.find_element_by_id("reg_email")
email.send_keys("evgeniy.online@mail.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("Mylosangeles6259119")
register_btn = driver.find_element_by_name("register")
register_btn.click()
time.sleep(15)

driver.quit()
