# -*- coding: utf-8 -*-
# Time    : 2023/11/26 12:46
# Author  : Walter
# File    : 百家号话题.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置浏览器驱动程序路径

s = Service(r'C:\Users\wuhengyu\Downloads\Compressed\chromedriver-win64\chromedriver-win64\chromedriver.exe')

# 创建浏览器实例
driver = webdriver.Chrome(service=s)
make_url = r'https://aigc.baidu.com/make'
driver.get(make_url)
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="welcome-navigator"]/div/span').click()
time.sleep(15)
driver.get(make_url)
time.sleep(3)
items = driver.find_elements(By.XPATH,
                             '//div[@class="overflow-auto flex-grow h-0 saas-scrollbar mt-[-4px] pl-[24px] pr-[10px] pb-[18px]"]')

contents = []
replaced_text = items[0].text
replaced_list = replaced_text.split('\n')
for i in range(len(replaced_list)):
    replaced_text = f"{replaced_list[i]},基于你的观点快速生成一篇动态。"
    contents.append(replaced_text)
print(contents)
