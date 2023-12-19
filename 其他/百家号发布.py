# -*- coding: utf-8 -*-
# Time    : 2023/11/26 10:35
# Author  : Walter
# File    : 百家号发布.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置浏览器驱动程序路径
s = Service(r'C:\Users\v_vhengyuwu\Downloads\Compressed\chromedriver-win64\chromedriver-win64\chromedriver.exe')

# 创建浏览器实例
options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')  # 禁用沙盒模式
# options.add_argument('--headless')  # 启用无头模式
driver = webdriver.Chrome(service=s, options=options)

# 打开页面
url = r'https://baijiahao.baidu.com/builder/rc/content?currentPage=1&pageSize=10&search=&type=&collection=&app_id=1776078385955258'
driver.get(url)
driver.maximize_window()
# 等待页面加载完成（可根据需要进行调整）
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div[2]/div[1]').click()
time.sleep(60)
# driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/button[2]').click()

# 使用XPath定位文本框
text_area = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="请输入内容创作、平台咨询等命令~"]'))
)

# 输入文本的列表
input_texts = ['甘肃6.2级地震已致数十人遇难：消防赶赴震中救援 地震来袭瞬间画面曝光, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'提高醉驾入刑门槛 早就该这么调整了, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'甘肃地震救援最大困难是低温, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'甘肃震区仍有可能发生5级强余震, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'12月18日最新：劳荣枝家属几点声明, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'甘肃积石山县发生6.2级地震, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'专家分析甘肃地震致重大伤亡原因, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'地震后学生操场裹被子烤火取暖, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'甘肃地震已致118人遇难, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'普京递交自我提名总统材料, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'男子低头接电话撞死老人, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'甘肃发布会现场为地震遇难者默哀, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'是否还会发生较大余震？甘肃省地震局：仍存在发生5级强余震的可能性, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'新疆阿图什5.5级地震, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'公租房小区被曝有多辆豪车停放, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'西安一高校宿舍门不开学生逃生, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'甘肃地震暖心瞬间, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'日本计划为“书法”申遗引争议, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'山东两幼师出租房内遇害, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'男子骑车接电话撞死老人后崩溃大喊, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'受地震影响黄河大桥出现裂缝, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'男子不满航班延误亮明网红身份维权, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'中国法学泰斗江平逝世, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'甘肃拨付临夏地震灾害资金, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'南方多地因雨雪天气停课, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'两部门向甘肃青海预拨2亿救灾款, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'冻雨灾害下停电4日的山西县城, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'传裁判文书网仅法院人士可在内网查询, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'地震时宿舍门不开学生砸玻璃逃生, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
'热力公司对小区改造供暖不知情, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本'][:25]

# 循环输入文本框
for text in input_texts:
    # 打开新的标签页
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header-wrapper"]/nav/div[2]/ul/li[3]/div').click()
    # 使用XPath定位并输入文本框内容
    text_area = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="请输入内容创作、平台咨询等命令~"]'))
    )
    time.sleep(3)
    text_area.clear()
    text_area.send_keys(text)
    text_area.send_keys(Keys.RETURN)
    # 等待页面加载完成（可根据需要进行调整）
    time.sleep(1)

'''
    try:
        # 等待按钮元素可见
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "一键发布")]')))
        # 执行相应的操作，比如点击按钮
        button.click()
    except Exception as e:
        print("点击失败,错误信息:")
        print(e)
    else:
        # # 刷新页面
        # # 定位一键发布按钮
        # button = driver.find_element(By.XPATH, '//button[contains(text(), "一键发布")]')
        # # 执行相应的操作，比如点击按钮
        # button.click()

        button = driver.execute_script('return document.evaluate("//button[contains(text(), \'一键发布\')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;')
        button.click()
    finally:
        time.sleep(2)
'''

time.sleep(10000)
# 关闭浏览器
driver.quit()
