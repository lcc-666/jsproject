from selenium import webdriver
import time
bro =webdriver.Chrome()

bro.get('https://www.taobao.com/')
time.sleep(3)
# bro.find_element_by_xpath('/html/body/div[15]/div/a').click()
# time.sleep(3)

search_input=bro.find_element_by_id('q')
search_input.send_keys('血滴子')
time.sleep(3)
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(3)
btn=bro.find_element_by_class_name('btn-search')
btn.click()