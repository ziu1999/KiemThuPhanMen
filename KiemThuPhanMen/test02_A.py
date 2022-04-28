from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('https://vlogtruyen.net')

test_driver.implicitly_wait(3)

# Step 2: Bấm vào button "HOT" trên thanh navigation
test_driver.find_element(By.XPATH, '/html/body/div[2]/div/a[1]').click()

test_driver.implicitly_wait(3)

# Step 3: Bấm vào select 'thể loại' chọn "Fantasy"
theloai = Select(test_driver.find_element(By.XPATH, '/html/body/div[5]/form/div[1]/select'))
theloai.select_by_index(2)

# Step 4: Bấm vào select 'nhóm dịch' chọn "Mega Team"
theloai = Select(test_driver.find_element(By.XPATH, '/html/body/div[5]/form/div[2]/select'))
theloai.select_by_index(1)

# Step 5: Bấm vào select 'trạng thái' chọn "Đã hoàn thành"
theloai = Select(test_driver.find_element(By.XPATH, '/html/body/div[5]/form/div[4]/select'))
theloai.select_by_index(1)

#lấy dữ liệu từ list
testXpath = test_driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/ul/li')
for testXpaths in testXpath:
    try:
        TenTruyen = testXpaths.find_element(By.XPATH, 'a[2]/h3').text
        Chapter = testXpaths.find_element(By.XPATH, 'span[1]/a').text
        Link1 = testXpaths.find_element(By.XPATH, 'a[1]').get_attribute('href')
        Link2 = testXpaths.find_element(By.XPATH, 'a[2]').get_attribute('href')
        print('Tên truyện : ', TenTruyen)
        print('chapter hiện tại: ', Chapter)
        print('Link của truyện (từ ảnh)', Link1)
        print('Link của truyện (từ chữ)', Link1)
        print('=======================')
    except NoSuchElementException:
        pass


#tắt testcase
# test_driver.close()
test_driver.quit()