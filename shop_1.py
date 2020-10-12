import time
from selenium import webdriver

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

html_btn = driver.find_element_by_css_selector(".cat-item-19 > a")
html_btn.click()
time.sleep(10)
count_elements = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
if len(count_elements) == 3:
    print("На странице отображается 3 товара")
else:
    print("Ошибка. На странице отображается: " + str(len(count_elements)))

driver.quit()
