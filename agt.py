#by zezen lovelive.net.cn
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
import os,time
chromedriver = ".\chromedriver.exe" 
os.environ["webdriver.Chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)
driver.get("http://bsdt.swun.edu.cn/SPCP/Web/")
driver.refresh() #刷新页面
driver.maximize_window() #浏览器最大化


driver.find_element_by_id("StudentId").send_keys("test")  #替换为自己的学号
driver.find_element_by_id("Name").send_keys("test")       #替换为自己的密码
code = driver.find_element_by_id("code-box").text
driver.find_element_by_id("codeInput").send_keys(code)


driver.find_element_by_id("Submit").click()

time.sleep(0.2) #等待网页加载

driver.find_element_by_id("platfrom0").click() #进入温度采集平台

time.sleep(0.2)

Select(driver.find_element_by_id('Temper1')).select_by_value("36")

Select(driver.find_element_by_id('Temper2')).select_by_value(str(random.randint(5,9)))  #温度在36.5-36.9随机生成

time.sleep(0.15)

driver.find_element_by_class_name("save_form").click() #提交
driver.get_screenshot_as_file('./sc.jpg')
