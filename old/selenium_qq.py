from selenium import webdriver
import time

bro=webdriver.Chrome()
bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')

bro.find_element_by_id('switcher_plogin').click()

username_tage=bro.find_element_by_id('u')
password_tage=bro.find_element_by_id('p')

username_tage.send_keys('2502247952')
time.sleep(2)
password_tage.send_keys('NRAHbsqt941')
time.sleep(2)

btn=bro.find_element_by_id('login_button')
time.sleep(2)

btn.click()