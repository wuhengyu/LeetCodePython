# -*- coding: utf-8 -*-
# Time    : 2023/6/11 20:06
# Author  : Walter
# File    : 微信阅读.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

'''
微信读书网页版通过发送请求到服务器来记录阅读时间。在上述请求中，我们可以看到一些关键参数，例如阅读时长rt和时间戳ts。基于这些参数，服务器可以计算阅读时间。

以下是从请求中提取的一些关键参数：

appId: 应用的ID
b: 书籍的ID
c: 章节的ID
ci: 当前页（章节）索引
co: 当前页（章节）总字数
sm: 当前阅读位置的开头文本
pr: 上一次阅读的页数（章节）索引
rt: 阅读时长，以秒为单位
ts: 发送请求时的时间戳（以毫秒为单位）
rn: 阅读进度的唯一数字
请求中的rt参数表示阅读时长。在这个例子中，rt的值是30，表示用户在这个页面上阅读了30秒。服务器会接收到这个请求，并使用ts参数中的时间戳来记录阅读时间。

当用户在网页版的微信读书中阅读书籍时，系统会周期性地发送这样的请求到服务器以记录阅读时间。服务器会在用户的阅读记录中累积这些阅读时长，并在合适的时候显示给用户。

请注意，这里的解释是基于你提供的请求示例。实际的实现可能会有所不同，但基本的原理应该是类似的。
'''
import json

import requests

url = "https://weread.qq.com/web/book/read"

payload = "{\"appId\":\"wb182564874663h982151229\",\"b\":\"b5142753643425f33626541664b416771417032366832366757326e763350508fa\",\"c\":\"65132ca01b6512bd43d90e3\",\"ci\":11,\"co\":3492,\"sm\":\"gg\",\"pr\":0,\"rt\":29,\"ts\":1686486642861,\"rn\":311,\"sg\":\"ab9cc8b5a5d0e1ae7282a68ecf186a6ccdb92aa4296d4b85966ccf79990e3c19\",\"dy\":0,\"fm\":\"epub\",\"ct\":1686484987,\"ps\":\"ff832e807a0d5ec5g01641d\",\"pc\":\"a63323b07a0d5eceg0140cb\",\"s\":\"88eeca85\"}"
payload_data = json.dumps(payload).encode('utf-8')
headers = {
    'authority': 'weread.qq.com',
    'cookie': 'RK=hFwsuCmvfp; ptcz=2c3163729b8c3d18f4f80c1d2887e937f541b7861e1d72407d0cf2b5894eb505; pgv_pvid=2616391862; tvfe_boss_uuid=a2afc8cee66a0889; o_cookie=578060214; fqm_pvqid=c0bf0533-05a4-4454-bedd-98791b21f289; iip=0; mobileUV=1_17a286f10a9_3b837; logTrackKey=5a81e7dfba8840669d0b71c4474b74f5; userty.core.p.bee5b2=__2VySWQiOiIyYjJhZGViMzVkNTZiY2MzNDIxZjllNzE2ZDQ3MjY2NSJ9eyJ1c; _hp2_id.1405110977=%7B%22userId%22%3A%227898247148763630%22%2C%22pageviewId%22%3A%224044141592377609%22%2C%22sessionId%22%3A%222869770881834814%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; eas_sid=B1I6i79203Z7l2q66317T4d2s1; psrf_qqopenid=49BBF25BA141CF9C7B5852A349D4BFC9; psrf_access_token_expiresAt=1690472332; psrf_qqrefresh_token=ED0A516259ABEA303DAA2066D89B341A; tmeLoginType=2; wxrefresh_token=; wxunionid=; psrf_qqunionid=3C37AB2132DFAE4F3348521C035A5444; psrf_qqaccess_token=4A0D255C4CD5FE3AC1F0C6691D2F8178; euin=7KSFoeCzow6P; wxopenid=; ptui_loginuin=578060214@qq.com; pac_uid=1_578060214; wr_gid=293002446; wr_vid=2500636; wr_pf=2; wr_rt=web%40nYGFa0NIzOqIQ0Mmd66_AL; wr_localvid=b51326a0626281cb510bdce; wr_name=Walter; wr_avatar=https%3A%2F%2Fwx.qlogo.cn%2Fmmhead%2FQ3auHgzwzM4ufJ9JPAQHgs33iclfHCtVuVQXWlhjznvS4oYEarkSnOA%2F0; wr_gender=1; OUTFOX_SEARCH_USER_ID_NCOO=1506683247.780918; qq_domain_video_guid_verify=4bc288c03b9c2c0f; wr_fp=4058703332; Hm_lvt_cda23766027f4145f8a9d2087788759e=1686410598; wr_theme=white; wr_skey=xeEf3zBl',
    'dnt': '1',
    'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
    'content-type': 'application/json;charset=UTF-8'
}

response = requests.request("POST", url, headers=headers, data=payload_data)

print(response.text)
