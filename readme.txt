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

0914 服务器后端需要注意的东西，需要添加或者完善的功能
    1、schema.sql文件的完善，现在创建数据库的方式是通过手动添加表格的方式，还不是通过代码自动添加。这一部分需要完善
    2、服务器后端代码的复用，需要在indoor和outdoor里面添加对应的handle_post()处理方法，indoor的比较复杂，因为涉及到多表
    操作，但是这里面没有涉及到表与表之间的耦合，所以现在问题应该不是很大
    3、整理database.py文件，在对应的查询以及响应的地方处理的不够。
    4、把服务器后端布置为多线程应用。
    5、导出数据数据文件（）  该功能待定。。。需要用的东西比较多。

