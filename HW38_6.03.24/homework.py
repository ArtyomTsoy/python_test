from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = 'C:/Users/Артем/Downloads/chromedriver_win32'

site = 'https://marketplace.me/'

selenium_service = Service(chrome)
driver = webdriver.Chrome()

driver.get(site)

prices = driver.find_elements(By.XPATH, '//div[@class="product-price"]')

for price in prices:
    print(price.text)

driver.quit()