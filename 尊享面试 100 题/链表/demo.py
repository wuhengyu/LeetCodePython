# -*- coding: utf-8 -*-
# Time : 2023/7/3 17:40
# Author : Walter
# File : demo.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置请求头，模拟浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 发送请求并获取网页内容，并按销售量排行对手机进行排序
url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&qrst=1&suggest=1.rem.0.0&wq=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&pvid=09bc6b9ceaed4eeb9a0db6ae47541eaa&psort=3&click=0'
response = requests.get(url, headers=headers)
html = response.content.decode('utf-8')

# 使用BeautifulSoup解析网页并提取数据
soup = BeautifulSoup(html, 'html.parser')
items = soup.select('.gl-item')

# 提取华为手机名称和价格信息，并将其保存到Pandas DataFrame中
data = []
for item in items:
    try:
        name = item.select('.p-name em')[0].text.strip()
        # 只保留手机型号信息
        # 将手机名称按照空格分割成一个列表
        name_list = name.split()
        # 找到包含“HUAWEI”的元素，并将其后面的元素拼接起来
        huawei_index = name_list.index("华为/HUAWEI")
        name = "".join(name_list[huawei_index:huawei_index + 2])

        price = item.select('.p-price strong')[0].i.text.strip()
        data.append({'name': name, 'price': price})
    except:
        pass
df = pd.DataFrame(data)

# 将数据保存到文件中
df.to_csv('吴博.txt', index=False)

# 绘制销售排名前十的手机销售柱状图
df['price'] = df['price'].str.replace(',', '').astype(float)
top10 = df[df['name'].str.contains('华为')].sort_values(by=['price'], ascending=False).head(10)

# 指定字体文件路径
font_path = '苹方黑体-极细-简.ttf'
font = FontProperties(fname=font_path)

# 绘制柱状图
plt.figure(figsize=(12, 8))  # 设置图表大小
plt.subplots_adjust(bottom=0.3)  # 调整x轴标签位置
plt.bar(top10['name'], top10['price'])
plt.xticks(rotation=90, fontproperties=font)
plt.title('销售排名前十的华为手机', fontproperties=font)
plt.xlabel('手机型号', fontproperties=font)
plt.ylabel('价格（元）', fontproperties=font)
plt.show()
