from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('https://vlogtruyen.net')
test_driver.implicitly_wait(4)

# Step 2: Nhập dữ liệu vào ô 'tìm kiếm'
test_driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/div[2]/div/form/div[1]/input').send_keys('Alibabcdef')


#tắt testcase
# test_driver.close()
# test_driver.quit()