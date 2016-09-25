阿里云服务器端后端程序说明：

1、主要功能：
	定时读取mysql的indoor数据内容，并且响应前端界面的get请求
	定时读取mysql的outdoor数据内容，并且相应前端界面的get请求
	定时读取mysql的control数据内容，并且相应前端界面的get请求；同时响应前端的post的get请求，保存到数据库
	
2、程序运行以及结构说明：
	软件及环境：Python2.7 Flask框架，Mysql5.6  MySQL-python 1.2.5
	运行说明：定位到main.py主函数的文件夹下面，打开cmd 输入： python main.py 回车即可
	服务器里面的位置：D:\software0726\server_back


3、数据库说明
	user：root
	password：xujiahui
	databaseName：kunshangreenhouse
	sheets：indoor outdoor control
	详细信息见schema.sql文件