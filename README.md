## AutoLogin
# v2.0.0版本重要说明
# 需自行注册百度AI平台获取token才能使用 详见 https://ai.baidu.com/forum/topic/show/867951 获取token后替换agt.py的第45行

自动登录西南民大的疫情采集平台并提交数据的脚本  
详细说明 https://lovelive.net.cn/2020/02/15/autologin/

需要安装python环境，并安装selenium库  
执行命令 pip install selenium  

本脚本依赖chrome实现，需要安装chrome浏览器，下载对应你电脑chrome版本的驱动并解压  
http://chromedriver.storage.googleapis.com/index.html  
并将驱动和脚本放在相同目录  

使用脚本前请将代码中的学号和密码改为自己的

使用cmd或powershell切换到脚本的目录 输入 python ./agt.py 运行提交温度脚本 输入 python ./agi.py 运行提交个人信息脚本 

当你登录温度平台的时候，会自动截图保存
  
## 版本更新说明   
v2.0.0 更新登录适应新验证码方式（只更新了agt.py
  
v1.3.0 适配更新后的平台
  
v1.2.0 添加自动截图功能，保存在当前目录下，温度在36.5-36.9之间随机生成
  
v1.1.0 添加自动提交个人信息脚本  
  
v1.0.1 优化部分代码  
  
v1.0.0 添加自动提交个人温度脚本  
