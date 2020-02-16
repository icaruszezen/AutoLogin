#by zezen lovelive.net.cn
from selenium import webdriver

import os,time
chromedriver = ".\chromedriver.exe" 
os.environ["webdriver.Chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)
driver.get("http://bsdt.swun.edu.cn/SPCP/Sys/Web/UserLogin.aspx") 
driver.refresh() #刷新页面
driver.maximize_window() #浏览器最大化


driver.find_element_by_id("StudentId").send_keys("test")  #替换为自己的学号
driver.find_element_by_id("Name").send_keys("test")       #替换为自己的密码
code = driver.find_element_by_id("code-box").text
driver.find_element_by_id("codeInput").send_keys(code)


driver.find_element_by_id("Submit").click()

time.sleep(0.1) #等待网页加载

#driver.find_element_by_class_name("layui-layer-btn0").click() #进入基本信息采集平台
driver.find_element_by_class_name("layui-layer-btn1").click() #进入温度采集平台

time.sleep(0.1)

driver.find_element_by_id("Temper").send_keys("36.5")  #输入温度

driver.find_element_by_class_name("save_form").click()

