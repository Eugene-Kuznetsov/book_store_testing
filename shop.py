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
book_btn = driver.find_element_by_css_selector(".post-181 > a")
book_btn.click()
HTML5_Forms_element = driver.find_element_by_css_selector(".product_title.entry-title")
HTML5_Forms_element_check = HTML5_Forms_element.text
print(HTML5_Forms_element_check)
if HTML5_Forms_element_check == "HTML5 Forms":
    print ("Заголовок книги называется HTML5 Forms!")
else:
    print("Заголовок книги НЕ соответствует надписи!")
driver.quit()
