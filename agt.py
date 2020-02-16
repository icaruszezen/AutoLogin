#by zezen lovelive.net.cn
from selenium import webdriver
import random
import os,time
chromedriver = ".\chromedriver.exe" 
os.environ["webdriver.Chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)
driver.get("http://bsdt.swun.edu.cn/SPCP/Sys/Web/UserLogin.aspx") #该处为具体网址
driver.refresh() #刷新页面
driver.maximize_window() #浏览器最大化


driver.find_element_by_id("StudentId").send_keys("test")  #替换为自己的学号
driver.find_element_by_id("Name").send_keys("test")       #替换为自己的密码
code = driver.find_element_by_id("code-box").text
driver.find_element_by_id("codeInput").send_keys(code)


driver.find_element_by_id("Submit").click()

time.sleep(0.1) #等待网页加载

driver.find_element_by_class_name("layui-layer-btn1").click() #进入温度采集平台

time.sleep(0.1)

driver.find_element_by_id("Temper").send_keys("36.",random.randint(5,9))  #输入温度


time.sleep(0.1)

localtime = time.localtime(time.time())
 
if localtime[3] <= 23 and localtime[3] >= 16 :
    if driver.find_element_by_class_name("layui-layer-title").text == "信息":
        driver.get_screenshot_as_file('./sc.jpg')
    else:
        driver.find_element_by_class_name("save_form").click() #提交
        time.sleep(0.1)
        driver.get_screenshot_as_file('./sc.jpg')
else:
    driver.find_element_by_class_name("save_form").click() #提交
