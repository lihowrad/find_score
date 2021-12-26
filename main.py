# -*- coding: utf-8 -*-
import time
import os
from scrapy.utils.project import get_project_settings
import pandas as pd
import winsound
import math

style = 2  # 告诉您成绩的方式, 1是直接告诉。 2是分析成绩和目标成绩差,分三档：好于预期，分差可接受，分差不可接受委婉传达成绩。3是自定义，如果不希望告诉您成绩，您手动查取，则请输入1,2，3以外的任何值
ori_score = 400  # style = 2 时 使用， 输入您的目标分数
acceptable_score_difference = -10  # style = 2 时 使用， 输入您的可接受分差

setting = get_project_settings()
print('程序开始执行,开始为您抓取相应网站的信息')
time.sleep(3)
print('程序当前运行参数如下:抓取网站地址:')
print(setting.get('URL'))
print('抓取时间间隔:'+'  '+str(setting.get('DELAY_TIME'))+'  '+'秒')
print('抓取次数:'+'  '+str(setting.get('DURATION')))
total = round(int(setting.get('DELAY_TIME'))*int(setting.get('DURATION'))/3600, 2)
print('本次程序预计运行:'+'  '+str(total)+'  '+'小时')

count = 1
while count != int(setting.get('DURATION')) + 1:
    print('第 %d 次爬取网站信息' % count)
    os.system("scrapy crawl Search -o result/export.csv")
    count += 1
    data = pd.read_csv('result/export.csv')
    result = data.iloc[-1, 0]
    if not isinstance(result, str):
        if math.isnan(result):
            print('开始尝试查询成绩')
            os.system('python scripts/sign-in.py')
            break
        if count != setting.get('DURATION') + 1:
            time.sleep(setting.get('DELAY_TIME'))

try:
    score = list(pd.read_csv('result/score.csv').iloc[:, 0])
    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    print('程序执行完成,结果成功输出')
    score_dir = {'政治': score[0], '英语': score[1], '数学': score[2], '专业课': score[3], '总分': score[4]}
    # score_dir = {'政治': 61, '英语': 84, '数学': 130, '专业课': 119, '总分': 60+84+130+119}

    # ******************************** 这里是自定义内容 *******************************************
    # 现在成绩已经保存在了score_dir中, 您希望如何查看成绩, 请调整以下代码
    time.sleep(3)
    os.system('cls')
    print('我已经偷偷帮您看了眼成绩~')
    # 如果您想直接查看成绩
    if style == 1:
        print('您的成绩为')
        print('政治:', score_dir['政治'])
        print('英语:', score_dir['英语'])
        print('数学', score_dir['数学'])
        print('专业课', score_dir['专业课'])
        print('总分', score_dir['总分'])

    # 如果您希望不直接获得成绩, 首先获得一些成绩相关的信息
    if style == 2:
        time.sleep(1)
        print('我来看看您和目标分数差多少')
        time.sleep(2)
        difference = int(score_dir['总分']) - ori_score
        if difference < 0:
            print('嗯~~您发挥的没有想象的好呢, 是否继续看下去?')
            time.sleep(2)
            a = input("输入1代表继续看下去,输入0代表放弃看下去,输入后按回车进行下一步:")
            if int(a) == 1:
                if difference < acceptable_score_difference:
                    print('您发挥的真的不太好呢, 是否还要继续看')
                    time.sleep(2)
                    b = input("输入1代表继续看下去,输入0代表放弃看下去,输入后按回车进行下一步:")
                    if int(b) == 1:
                        print('您的成绩为')
                        print('政治:', score_dir['政治'])
                        print('英语:', score_dir['英语'])
                        print('数学', score_dir['数学'])
                        print('专业课', score_dir['专业课'])
                        print('总分', score_dir['总分'])
                    else:
                        print('请不要太难过,人生无处不青山')
                else:
                    print('虽然没有达到预期, 但是您和预期差的不多呢, 您的成绩为:')
                    print('政治:', score_dir['政治'])
                    print('英语:', score_dir['英语'])
                    print('数学', score_dir['数学'])
                    print('专业课', score_dir['专业课'])
                    print('总分', score_dir['总分'])
            else:
                print('请不要太难过,人生无处不青山')
        else:
            print('嗯~~您发挥的和预期一样好呢')
            time.sleep(2)
            print('您的成绩为')
            print('政治:', score_dir['政治'])
            print('英语:', score_dir['英语'])
            print('数学', score_dir['数学'])
            print('专业课', score_dir['专业课'])
            print('总分', score_dir['总分'])

    if style == 3:
        # 请在此处使用您希望获得成绩的方法
        # 可能有用的提醒:score_dir以字典的形式储存着您的成绩, 其中字典的键包括"政治""英语""数学""专业课""总分", 字典的值是字符串形式(重要), 不要忘记用int转换
        pass
except FileNotFoundError:
    pass

print('本程序已经全部完成,希望能够给予您一点点小小的帮助')



