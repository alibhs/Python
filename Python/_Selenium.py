from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/Ali/Desktop/chromedriver.exe")
url="http://www.reuters.com/"

# driver.get(url)
# time.sleep(3)
# driver.maximize_window()
# time.sleep(3)
# url="http://www.bloomberg.com/middleeast"
# driver.get(url)
# driver.back()
# time.sleep(3)
# driver.forward()
# driver.close()

driver.get(url)
# print(driver.page_source)
time.sleep(3)
driver.refresh()
time.sleep(2)
driver.close()