# 复旦考研初试成绩查询以及成绩告知 #
关键词：scrapy, selenium
## 程序介绍: ##
本程序是专门用于帮助考研fdu的同学查分的爬虫程序, 它按照事先设定好的频率和次数爬取成绩查询页面, 当发现成绩放出时会通过事先给定的个人信息自动登入成绩查询系统并获得成绩, 最后按照使用者的意愿告诉使用者成绩情况, 或者仅仅是提醒使使用者成绩已经出来, 让使用者自行查询成绩。  
总的来说两种功能：1、获得出分的第一手消息。2、抓取使用者的成绩，并以合适的方式告知使用者（类似与网上代找成绩）
## 程序所需要的电脑环境以及相关库: ##

1、python3.8（安装pycharm最好，直接用cmd运行也可以，用cmd运行时请务必注意“注意事项”中的第六条）  
2、pandas  
3、Pillow (或者叫PIL)  
4、selenium 3  
5、chromedriver（本程序使用chrome浏览器，如果是其他浏览器请务必注意“注意事项”中的第三条）  
6、numpy  
7、scrapy 2.4.1  
8、Tesseract-OCR 以及pytesseract  
9、opencv-python（就是opencv，或者叫cv2)  
## 程序如何使用: ## 
项目中有两个文件需要使用者打开并修改参数:  
1、main.py：在项目的根目录中， 需要修改的参数包括style、ort_score、acceptable_score_difference三项。当然，如果不需要程序帮您“委婉”的查询成绩，后两项可以不需要更改  
  
2、settings.py：在find_score文件夹中，这一文件是爬取网页相关的参数，包括抓取时间设置的两个参数：delaytime和duration。发送请求的两个参数，包括网站地址url和user-agent。以及个人信息的两个参数nd和password。基础设置请尽量不做更改。  
  
相关参数的作用已经在程序中注释了  
  
在设置完成后，直接通过pycharm运行main.py或者用cmd打开main.py都可以  
## 注意事项: ##
1、（重点）关于查询的频率和次数：请在find_score的setting.py内更新, delay_time代表间隔多少秒查询一次, duration代表一共进行几次查询,  可以根据个人喜好进行修改。初始值是测试用的，仅查两次，每次之间间隔5秒。建议间隔几分钟，查询个几百次，跑个几天一直跑到信息更新（笑）。上述建议只针对电脑hold得住的同学，和我一样用办公本的请无视。  
2、关于是否违法：虽然成绩查询网站有设置验证码，但是程序在爬取信息的时候遵循robots.txt的要求，因此不会违法。使用selenium抓取验证码进行模拟登陆本身上就是模仿用户打开浏览器登陆的过程。当然，如果说了这些您还是怕有封号的危险，或者担心被盗用个人信息可以不使用本程序的自动爬取成绩的功能，然而本程序通过不断爬取网站获得出分的第一手消息的功能中没有用到任何账号或者个人信息，请放心使用。  
3、（重点）本程序使用chrome浏览器，用到的webdriver是chromedriver， 如果是其他浏览器的话，请自行下载对应的驱动器，并修改scripts文件夹中sign-in.py文件中的对应代码  
`options = webdriver.ChromeOptions()`  
`browser = webdriver.Chrome(chrome_options=options)`  
4、如果有bug等相关问题。请联系作者。作者QQ:1229236880, 添加好友请说明来意
5、仅用于考研复旦的朋友。本程序仅用于娱乐  
5、修改useragent：不同的操作系统以及浏览器类型会产生不同的useragent，如何查找自己的useragent请直接百度“useragent”。  
6、(2.25补充的bug)本程序在pycharm上完美运行， 在命令行上运行或者直接用python运行时， 请将find_score文件夹中的find_score文件夹放置在自己python所在文件夹下, Lib文件夹中的site-packages文件夹中
