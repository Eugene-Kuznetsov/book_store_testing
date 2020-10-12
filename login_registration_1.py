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
time.sleep(5)
logout_element = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout > a")
logout_element_check = logout_element.text
print(logout_element_check)
if logout_element_check == "Logout":
    print ("Данный элемент присутствует на странице!")
else:
    print("Данный элемент на странице не найден!")
driver.quit()

