# AutoLogin

自动登录西南民大的疫情采集平台并提交数据的脚本  
详细说明 https://lovelive.net.cn/2020/02/15/autologin/

需要安装python环境，并安装selenium库  
执行命令 pip install selenium  

本脚本依赖chrome实现，需要安装chrome浏览器，下载对应你电脑chrome版本的驱动并解压  
http://chromedriver.storage.googleapis.com/index.html  
并将驱动和脚本放在相同目录  

使用脚本前请将代码中的学号和密码改为自己的

使用cmd或powershell切换到脚本的目录 输入 python ./agt.py 运行提交温度脚本 输入 python ./agi.py 运行提交个人信息脚本 


  
# 版本更新说明  

v1.1.0 添加自动提交个人信息脚本  
  
v1.0.1 优化部分代码  
  
v1.0.0 添加自动提交个人温度脚本  
