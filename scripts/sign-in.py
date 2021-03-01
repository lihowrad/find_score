# -*- coding: utf-8 -*-
from scrapy.utils.project import get_project_settings
from PIL import Image
import cv2
from selenium import webdriver
import time
import numpy as np
import pytesseract
import pandas as pd
import os

settings = get_project_settings()


def treat_validateCode(br):
    br.maximize_window()
    br.get_screenshot_as_file('screenshot.png')
    location = br.find_elements_by_id('imageID')[0].location
    size = br.find_elements_by_id('imageID')[0].size

    left = location['x'] + 20
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = Image.open('screenshot.png').crop((left, top, right, bottom))
    image.save('code.png')

    img = Image.open('code.png')
    img = np.array(img)
    h, w = img.shape[:2]
    for y in range(0, w):
        for x in range(0, h):
            if y < 2 or y > w - 2:
                img[x, y] = 255
            if x < 2 or x > h - 2:
                img[x, y] = 255
    cv2.imwrite('code_done.png', img)
    code = pytesseract.image_to_string('code_done.png')
    return br, code


re_retry = False
i = 0
while not re_retry and i < 5:
    i += 1
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent="' + settings.get('USER_AGENT') + '"')
    options.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(settings.get('URL'))  # 请求登录界面
    username = browser.find_elements_by_id('username')[0]  # 获取username的input标签
    time.sleep(0.5)
    username.send_keys(settings.get('ND'))
    time.sleep(0.5)
    password = browser.find_elements_by_id('password')[0]  # 获取password的input标签
    password.send_keys(settings.get('PASSWORD'))
    time.sleep(0.5)
    retry = True
    times = 0
    while retry and times < 5:
        times += 1
        browser, Code = treat_validateCode(browser)
        validateCode = browser.find_elements_by_id('validateCode')[0]
        time.sleep(0.5)
        validateCode.clear()
        validateCode.send_keys(Code)  # 输入验证码
        time.sleep(0.5)
        # browser.find_elements_by_id('loginIt')[0].click()
        if not browser.find_elements_by_id('errorInfo'):
            retry = False
    if times >= 5:
        re_retry = False
        browser.close()
        print('稍安勿躁, 验证码识别能力有限, 正在重启验证码识别程序, 这是重新运行的第' + str(i) + '遍')
    else:
        re_retry = True
        print('已进入成绩页面')
        # ****************** 处理成绩 ***************************************

        zheng_zhi = browser.find_elements_by_xpath('//div[@class="line"]//tr[3]/td[2]')[0].text.strip()
        ying_yu = browser.find_elements_by_xpath('//div[@class="line"]//tr[4]/td[2]')[0].text.strip()
        shu_xue = browser.find_elements_by_xpath('//div[@class="line"]//tr[5]/td[2]')[0].text.strip()
        zhuan_ye_ke = browser.find_elements_by_xpath('//div[@class="line"]//tr[6]/td[2]')[0].text.strip()
        total = browser.find_elements_by_xpath('//div[@class="line"]//tr[7]/td[2]')[0].text.strip()
        browser.close()
        score = 'result/score.csv'
        data = pd.DataFrame({"分数": [zheng_zhi, ying_yu, shu_xue, zhuan_ye_ke, total]})
        data.to_csv(score, index=False)
        print('分数已保存')
        os.remove("code_done.png")
        os.remove("code.png")
        os.remove('screenshot.png')

if i >= 5:
    print('很抱歉, 信息登入失败, 请检查个人信息是否正确, 如果正确请联系制作者询问原因')
