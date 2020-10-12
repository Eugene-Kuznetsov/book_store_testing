import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
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

sorting = driver.find_element_by_css_selector(".orderby :nth-child(6)")
sorting_selected = sorting.get_attribute("selected")
print("Value of sorting: ", sorting_selected)
if sorting_selected is None:
    print("Сортировка по умолчанию НЕ from HIGH to LOW")
else:
    print("Сортировка from HIGH to LOW выбрана по умолчанию")

sorting_high_low = driver.find_element_by_class_name("orderby")
select = Select(sorting_high_low)
select.select_by_value("price-desc")
sorting_1 = driver.find_element_by_css_selector(".orderby :nth-child(6)")
sorting_1_selected = sorting_1.get_attribute("selected")
print("Value of sorting: ", sorting_1_selected)
if sorting_1_selected is None:
    print("Сортировка выбрана НЕ from HIGH to LOW")
else:
    print("Сортировка выбрана from HIGH to LOW")

driver.quit()
