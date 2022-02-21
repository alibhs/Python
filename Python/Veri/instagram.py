from Instabilgi import kullanıcıadı,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver=webdriver.Chrome(executable_path=r"C:/Users/Ali/Desktop/chromedriver.exe",chrome_options=options)
url = "https://www.instagram.com/accounts/login/"

driver.get(url)

time.sleep(2)

ka=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
ka.send_keys(kullanıcıadı)

sif=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
sif.send_keys(sifre)
sif.send_keys(Keys.ENTER)