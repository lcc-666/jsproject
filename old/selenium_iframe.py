from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro=webdriver.Chrome()

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

actiom=ActionChains(bro)
actiom.click_and_hold(div)

for i in range(5):
    actiom.move_by_offset(50,0).perform()
    sleep(0.5)

actiom.release()

#bro.quit()