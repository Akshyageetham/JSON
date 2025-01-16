
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/inventory.html')

print(driver.title)
print(driver.current_url)
time.sleep(3)

page_content = driver.find_element(By.XPATH, '/html/body').text
file = open('result.txt', 'w')
file.write(page_content)
file.close()

