# -*- coding: utf-8 -*-
# Time    : 2023/7/3 23:02
# Author  : Walter
# File    : demo2.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import pandas as pd
import matplotlib.pyplot as plt

# 创建数据框
data = {
    "name": ["华为/HUAWEIP60", "HUAWEInova", "HUAWEIMate", "HUAWEIMate", "华为/HUAWEIP50",
             "HUAWEInova", "华为/HUAWEIP60", "HUAWEIMate", "华为/HUAWEIMate", "华为/HUAWEIP60"],
    "price": [4888.0, 1699.0, 4550.0, 4899.0, 3988.0, 2399.0, 7288.0, 6199.0, 8999.0, 7988.0]
}
df = pd.DataFrame(data)

# 统计销售量并按照销售量排序
df["sales"] = df["price"]
top10 = df.sort_values("sales", ascending=False).head(20)

# 创建柱状图
plt.bar(top10["name"], top10["sales"])
plt.xticks(rotation=90)
plt.ylabel("Sales")
plt.title("Top 10 Selling Products")
plt.show()
