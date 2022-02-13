from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches',['enable-logging '])
driver=webdriver.Chrome(executable_path=r"C:/Users/Ali/Desktop/chromedriver.exe",chrome_options=options)
url="https://www.dr.com.tr/"

driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
kitap=driver.find_element_by_xpath("/html/body/div/header/div[4]/div[2]/ul[1]/li[1]/a")
kitap.click()
time.sleep(2)

kitapara=driver.find_element_by_css_selector("body > div > header > div.site-header-center.bg-c255.py-10 > div > div > div.search.col-12.col-lg-7.mt-10.mt-lg-0.dr-flex > div.search-wrapper.col-12.col-lg-10.p-0 > input")
kitapara.send_keys("Şiir")
time.sleep(2)
kitapara.send_keys(Keys.ENTER)

for i in range(1,10):
    bilgi=driver.find_element_by_xpath("/html/body/div/div[2]/div/div/main/div[3]/div[1]/div[{}]/div/div[2]/div[1]/a".format(i))
    print(bilgi.text)

driver.close()