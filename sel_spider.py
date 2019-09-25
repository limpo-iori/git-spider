from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys("python")
driver.find_element_by_("s_btn_wr").click()
driver.save_screenshot('1.png')