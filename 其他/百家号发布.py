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
input_texts = [
                  '穿交警制服人员当街打架？当地回应, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '广西一婚车漏油被鞭炮引燃, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '2人因直播造谣有8.2级余震被拘, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '警方通报19岁男子砍伤3名女子, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '金田村的日与夜：一个青海村庄地震后与砂涌赛跑的抢险片段, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '淮安体育运动学校原校长戴红萍被查, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '甘肃地震互助, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '库克发文谈甘肃地震, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '福建泉州一化工厂起火 有人员受伤, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '男子拆快递时意外收到2箱现金, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '宁夏文旅邀董宇辉再来宁夏, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '相声的起源｜相声最早是为了逗笑贵族？跟笑话是一回事？, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '青海一村震后山体滑坡 20人失联, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '甘肃6.2级地震救援现场, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '地震后村庄遭砂涌：泥浆浪头高3米, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '小伙为省3000元出国旅游被卖3次, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '法学泰斗江平逝世, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '惠州海景房：5折随意选 最低15万, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '湖北一银行行长在荒郊自杀, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '临夏与1240名考研生逐一建联, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '网友吐槽买了一盒金车厘子583元, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '传临夏8.2级余震造谣者被行拘, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '金车厘子300元一斤, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '惠州15万可买入门级海景房, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '合肥地铁系统瘫痪？男子造谣被拘, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '韩国仁川刺激生育, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '黑龙江一汽车预热后爆燃, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '人类和鲸鱼首次成功“对话”, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '甘肃青海受灾地区通信正常, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本',
                  '鳖盖被压坏男子索赔两万多吓坏司机, 基于这个社会话题的观点快速生成一篇动态，图片贴合主题，生成动态内容+图片，不要纯文本'][
              :25]

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
