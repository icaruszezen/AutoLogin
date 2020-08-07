# encoding:utf-8

import requests
import base64
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
import os,time
from PIL import Image

chromedriver = ".\chromedriver.exe" 
os.environ["webdriver.Chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)
driver.get("http://bsdt.swun.edu.cn/SPCP/Web/")
driver.refresh() #刷新页面
driver.maximize_window() #浏览器最大化


driver.find_element_by_id("StudentId").send_keys("test")  #test替换为自己的学号
driver.find_element_by_id("Name").send_keys("test")       #test替换为自己的密码

def isElementExist(css): #判断验证码是否正确
    try:
        driver.find_element_by_class_name(css)
        return True
    except:
        return False

def Code(): #输入验证码函数
    driver.save_screenshot('.\\printscreen.png')
    imgelement = driver.find_element_by_id('code-box')  # 定位验证码
    location = imgelement.location  # 获取验证码x,y轴坐标
    size = imgelement.size  # 获取验证码的长宽
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    i = Image.open(".\\printscreen.png")  # 打开截图
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4=frame4.convert('RGB')
    frame4.save('.\\save.jpg')
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    f = open('.\\save.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img,"language_type":"ENG"}
    #token须在百度ai平台注册免费获取，替换下面的test
    access_token = 'test'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
    code = response.json().get("words_result")[0].get("words")
    code = code.replace(' ', '')
    print(code)
    driver.find_element_by_id("codeInput").send_keys(code)

Code()
driver.find_element_by_id("Submit").click()
time.sleep(0.2) #等待网页加载
while(isElementExist("layui-m-layercont")):
    time.sleep(0.5)
    driver.find_element_by_class_name("layui-m-layerbtn").click()
    time.sleep(0.3) #等待网页加载
    driver.find_element_by_id("Name").send_keys("210012")
    driver.find_element_by_id("codeInput").clear()
    Code()
    driver.find_element_by_id("Submit").click()
    time.sleep(0.3) #等待网页加载


time.sleep(0.2) #等待网页加载

driver.find_element_by_id("platfrom1").click() #进入温度采集平台

time.sleep(0.2)

Select(driver.find_element_by_id('Temper1')).select_by_value("36")

Select(driver.find_element_by_id('Temper2')).select_by_value(str(random.randint(5,9)))  #温度在36.5-36.9随机生成

time.sleep(0.15)
driver.get_screenshot_as_file('./sc.jpg') #截图
driver.find_element_by_class_name("save_form").click() #提交
driver.get_screenshot_as_file('./sc.jpg')

