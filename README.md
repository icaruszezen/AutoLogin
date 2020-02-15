# AutoLogin
自动登录西南民大的疫情采集平台并提交数据的脚本  
详细说明 https://lovelive.net.cn/2020/02/15/autologin/

需要安装python环境，并安装selenium库  
执行命令 pip install selenium  

本脚本依赖chrome实现，需要安装chrome浏览器，下载对应你电脑chrome版本的驱动并解压  
http://chromedriver.storage.googleapis.com/index.html  
并将驱动和脚本放在相同目录  

使用脚本前请将代码中的学号和密码改为自己的

使用cmd或powershell切换到脚本的目录 输入指令python ./agt.py即可自动登录

目前仅支持自动登录提交温度，可自行修改提交个人信息版本或等待我后续更新
