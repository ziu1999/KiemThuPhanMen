from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('https://vlogtruyen.net')


#Step 2: Bấm vào button "Đăng nhập"
test_driver.find_element(By.CSS_SELECTOR, '#btnLogin').click()

test_driver.implicitly_wait(4)

# Step 3: Nhập username
test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[1]/div[1]/input').send_keys('dfsdfsdfs')


# Step 4: Nhập password
test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[1]/div[2]/input').send_keys('hidordasdi123')

# Step 5: Bấm vào button "Đăng nhập"
test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[1]/div[3]/button').click()


#tắt testcase
# test_driver.close()
# test_driver.quit()