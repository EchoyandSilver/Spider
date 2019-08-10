# Spider
## 爬虫列表(scrapy框架) ##
* 01-古诗文网爬虫

	```
	注释：爬取出的数据存放在json文件内。
	```

* 02-猎云网爬虫

	```
	注释：爬取出的数据存放在mysql数据库内。建表规则见项目内CreateSyntax.md。
	```

* 03-模拟登录GitHub

	```
	注释：模拟登录GitHub，将登陆后的个人界面html文本保存在html文件内。使用方法名：scrapy.FormRequest.from_response。
	```

* 04-下载器中间件

	```
	注释：修改下载器中间件文件middlewares.py，达到随机更换user-agent和代理ip。
	```
	
* 05-文件下载爬虫

	```
	注释：爬取网站（http://zcool.com.cn/），爬取网站图片，按照指定路径存储在本地。
	```
	
* 06-猎聘网爬虫

	```
	注释：
	1、爬取全国python相关职位信息，将爬去的数据保存在mysql数据库内。建表规则见项目内CreateSyntax.md。
	2、随机更换user-agent请求头。
	3、随机更换IP代理。创建一个多线程，专门用来管理代理的；管理方式：只要这个代理的时间超过了1分钟，或者是这个代理被拉黑了，那么在多线程中就要更换代理；本项目使用“极光代理”。
	```
	
* 07-链家网爬虫

	```
	注释：
	1、爬取链家网全国出租房信息，将爬去的数据保存在mysql数据库内。建表规则见项目内CreateSyntax.md。
	2、随机更换user-agent请求头。
	3、添加lianjia分布式爬虫，并添加环境搭建及分布式爬虫部署流程：分布式爬虫部署流程.md。
	```

## 爬虫(数据解析方法及案例) ##
* 常用解析工具

解析工具|解析速度|使用难度
---|:--:|---:
BeautifulSoup|最慢|最简单
lxml|快|简单
正则表达式|最快|最难

### 01-正则表达式解析(re模块使用) ###
* 1、正则表达式re模块使用

* 2、糗事百科爬虫

* 3、赶集网爬虫

### 02-BeautifulSoup4的使用（bs4） ###
* 1、bs4模块使用

* 2、bs4-豆瓣top250爬虫

* 3、bs4-快代理ip爬取





	