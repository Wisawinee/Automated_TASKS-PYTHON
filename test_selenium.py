from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")
url = "https://th.investing.com/crypto/bitcoin/chart"
driver.get(url)

bitcoin_price = driver.find_element_by_id('last_last').text
print(bitcoin_price)