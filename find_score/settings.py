# -*- coding: utf-8 -*-
# ********************************基础设置******************************************************************

BOT_NAME = 'find_score'
SPIDER_MODULES = ['find_score.spiders']
NEWSPIDER_MODULE = 'find_score.spiders'# Obey robots.txt rules
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'INFO'
LOG_ENABLED = False
# ********************************抓取时间设置**************************************************************
# int 类型, 代表间隔多少秒再次进行爬取
DELAY_TIME = 2
# 持续时间, 表示一共进行多少次爬取
DURATION = 2
# ********************************web设置*******************************************************************
# 查询成绩网站的url
URL = 'https://gsas.fudan.edu.cn/sscjcx/index'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# *******************************私人信息设置***************************************************************
# 准考证号
ND = '*****************'
# 身份证号
PASSWORD = '******************'
