# -*- coding: utf-8 -*-
# Time : 2023/7/3 17:40
# Author : Walter
# File : demo.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :

import requests
from bs4 import BeautifulSoup

url = "https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&qrst=1&suggest=1.rem.0.0&wq=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&pvid=09bc6b9ceaed4eeb9a0db6ae47541eaa&psort=3&click=0"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all("div", class_="gl-i-wrap")
result = []
for item in items:
    name = item.find("div", class_="p-name").text.strip()
    price = item.find("strong", class_="J_price").text.strip()
    result.append({"name": name, "price": price})

with open("吴博2.txt", "w", encoding="utf-8") as f:
    for item in result:
        f.write(f"{item['name']} {item['price']}\n")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("吴博.txt", sep=" ", header=None, names=["name", "price"])
df["sales"] = df["price"].astype(float)

top10 = df.sort_values("sales", ascending=False).head(10)
plt.bar(top10["name"], top10["sales"])
plt.xticks(rotation=90)
plt.ylabel("Sales")
plt.title("Top 10 Selling Products")
plt.show()
