# -*- coding: utf-8 -*-
# Time : 2023/11/28 14:13
# Author : Walter
# File : 小宇宙下载.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :

import re
import requests
from urllib.parse import urlparse

def extract_links(url):
    response = requests.get(url)
    content = response.text
    pattern = r'<enclosure url="(.*?)" type="audio/mp4"'
    links = re.findall(pattern, content)
    return links[0:1]

def extract_title(url):
    response = requests.get(url)
    content = response.text
    pattern = r'<item>\n\s*<title>(.*?)<\/title>'
    # title = re.search(pattern, content).group(1)
    titles = re.findall(pattern, content)
    # print(titles[0:1])
    return titles

# def download_and_merge(links, filename):
#     parsed_url = urlparse(link)
#     clean_link = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
#     response = requests.get(clean_link)
#
#     with open(filename, "wb") as file:
#         file.write(response.content)

# 要提取链接的地址
url = "https://feed.xyzfm.space/6tpl4er6v3kk"

# 调用函数提取链接
extracted_links = extract_links(url)

# 去除查询字符串
cleaned_links = [re.sub(r"\?.*", "", link) for link in extracted_links]

# 调用函数提取名称
titles = extract_title(url)

# 循环下载
for link, title in zip(extracted_links, titles):
    filename = f"{title}.m4a"
    # 下载并保存文件
    response = requests.get(link)
    with open(filename, "wb") as file:
        file.write(response.content)