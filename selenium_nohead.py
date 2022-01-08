from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

options=ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])


bro=webdriver.Chrome(chrome_options=chrome_options,options=options)

bro.get('https://www.baidu.com')

print(bro.page_source)
time.sleep(3)
bro.quit()