from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()
test_driver.implicitly_wait(4)

#Step 1: Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('https://vlogtruyen.net')
test_driver.implicitly_wait(4)

#Step 2: Bấm vào button "tìm kiếm"
test = test_driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/div[2]/div/form/div[1]/div[2]/button')
test.click()
#tắt testcase
# test_driver.close()
# test_driver.quit()