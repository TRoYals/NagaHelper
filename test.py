from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=/Users/fuqixuan/Library/Application Support/Google/Chrome/Default')
option.add_experimental_option("detach", True)
 #加载前面获取的 个人资料路径
driver = webdriver.Chrome(chrome_options=option)#/Users/fuqixuan/Downloads/chromedriver_mac_arm64
driver.get('https://naga.dmv.nico/naga_report/order_form/')
input_field = driver.find_element(By.NAME, "haihu_url")
input_field.send_keys('What is the capital of France?')

print(input_field.text)
button = driver.find_element(By.CSS_SELECTOR, ".mt-3")
driver.implicitly_wait(10)

restNp =driver.find_element(By.CLASS_NAME, "h4")
print(restNp.text)
button.click()
driver.implicitly_wait(30)

driver.get('https://naga.dmv.nico/naga_report/order_report_list/')
link = driver.find_element(By.CSS_SELECTOR, "#myTabContent > div:nth-child(1) > div.text-center > div > table > tbody > tr > td.px-0 > div > a")

print(link.get_attribute('href'))