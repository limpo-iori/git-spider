from selenium import webdriver
import time
url = 'https://shopee.com.my/'
brower = webdriver.Chrome()
brower.get(url)
time.sleep(10)
brower.save_screenshot('capture.jpg')
brower.close()