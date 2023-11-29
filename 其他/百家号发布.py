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
options.add_argument('--no-sandbox')  # 禁用沙盒模式
# options.add_argument('--headless')  # 启用无头模式
driver = webdriver.Chrome(service=s, options=options)

# 打开页面
url = r'https://baijiahao.baidu.com/builder/rc/content?currentPage=1&pageSize=10&search=&type=&collection=&app_id=1776078385955258'
driver.get(url)
driver.maximize_window()
# 等待页面加载完成（可根据需要进行调整）
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div[2]/div[1]').click()
time.sleep(20)
# driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/button[2]').click()

# 使用XPath定位文本框
text_area = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="请输入内容创作、平台咨询等命令~"]'))
)

# 输入文本的列表
input_texts = ['女儿高烧40度 妈妈捏着取的1600号,基于你的观点快速生成一篇动态。',
               '男方给30万彩礼女方却只拿到20万,基于你的观点快速生成一篇动态。',
               '杭州女童坠亡案：保姆女儿反诉雇主,基于你的观点快速生成一篇动态。',
               '马斯克婉拒哈马斯邀访加沙,基于你的观点快速生成一篇动态。',
               '男子住88元酒店后带走150元被子,基于你的观点快速生成一篇动态。',
               '京东市值一年蒸发700亿,基于你的观点快速生成一篇动态。',
               '12岁女生上体育课时猝死,基于你的观点快速生成一篇动态。',
               '外卖员当街下跪向交警求情 平台回应，基于你的观点快速生成一篇动态',
               '从阿里云到滴滴崩溃一夜,基于你的观点快速生成一篇动态。',
               '大学生独游华山坠崖失联10天,基于你的观点快速生成一篇动态。',
               '雷军个人向武汉大学捐赠13亿元,基于你的观点快速生成一篇动态。',
               '男子中2.6亿后次日凌晨准时上班,基于你的观点快速生成一篇动态。',
               '马云谈拼多多市值逼近阿里：祝贺，基于你的观点快速生成一篇动态',
               '巴菲特副手查理·芒格离世,基于你的观点快速生成一篇动态。',
               '网友举报转转出具阴阳检测报告,基于你的观点快速生成一篇动态。',
               '张艺谋获终身成就奖,基于你的观点快速生成一篇动态。',
               '华为重新洗牌汽车行业,基于你的观点快速生成一篇动态。',
               '朝鲜在联合国为卫星发射辩护,基于你的观点快速生成一篇动态。',
               '胃癌发现时大多是中晚期,基于你的观点快速生成一篇动态。',
               '男子买烟没付钱店主怒发视频,基于你的观点快速生成一篇动态。',
               '日赚3000元月赚几十万,基于你的观点快速生成一篇动态。',
               '海关总署新增10家牛肉输华企业,基于你的观点快速生成一篇动态。'][:20]

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
    time.sleep(2)

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
# wait = WebDriverWait(driver, 10)
# button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "一键发布")]')))
# # 执行相应的操作，比如点击按钮
# button.click()

time.sleep(2000)
# 关闭浏览器
driver.quit()
