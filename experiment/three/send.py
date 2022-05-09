"""
我已经手动确定了驱动的路径，不需要将其配置到python解释环境之中，需要将send同目录下的chromedriver一同拷贝
chrome版本采用最新的101
selenium使用selenium3，如果使用selenium4会出现兼容问题
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('https://email.163.com/')

bro.switch_to.frame(0)

# username_tage = bro.find_element_by_name('email')
username_tage = bro.find_element(by=By.NAME,value="email")
password_tage = bro.find_element(by=By.NAME,value="'password'")

username_tage.send_keys("lcc2502247952")
password_tage.send_keys("NRAHbsqt941")
time.sleep(2)

btn = bro.find_element(by=By.XPATH,value='//*[@id="dologin"]')
btn.click()
time.sleep(2)

write=bro.find_element(by=By.XPATH,value="//*[@id='_mail_component_149_149']/span[2]")
write.click()

time.sleep(2)
bro.find_element(by=By.CLASS_NAME,value='nui-editableAddr-ipt').send_keys("2502247952@qq.com")
bro.find_elements(by=By.CLASS_NAME,value="nui-ipt-input")[2].send_keys("spider")
time.sleep(3)
bro.switch_to.frame(3)

bro.find_element(by=By.CLASS_NAME,value="nui-scroll").send_keys("spider")
bro.switch_to.default_content()
time.sleep(2)
bro.find_element(by=By.XPATH,value='//*[@id="_mail_button_8_275"]/span[2]').click()

