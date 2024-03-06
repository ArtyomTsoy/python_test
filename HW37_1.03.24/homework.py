from selenium import webdriver

driver = webdriver.Chrome()

url = "https://apecon.ru/prognoz-kursa-dollara-k-tenge-na-zavtra-nedelyu-mesyats-gody"
driver.get(url)

dollar_element = driver.find_element_by_xpath("//div[@class='txt']/p[1]/strong")

dollar_to_tenge_rate = dollar_element.text

print("Курс доллара к тенге", dollar_to_tenge_rate)

driver.quit()