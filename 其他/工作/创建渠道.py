# -*- coding: utf-8 -*-
# Time : 2023/8/31 14:53
# Author : Walter
# File : 创建渠道.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :
import random

import requests

for i in range(1, 200):
    url = "https://admin.qidian.qq.com/tp/wpa/newCreate"

    channel_number = random.randint(18, 3000)
    # payload = f"name=%E7%BD%91%E9%A1%B5H5{channel_number}&cate=7&type=10&scene=3&sideBarId=&interactNavId=&roleIM%5BrobotNav%5D%5BrobotNavMenuSwitch%5D=0&roleIM%5Bvalue%5D=4&roleIM%5BmsgDisplayed%5D=0&roleIM%5Buin%5D=9936786593&roleIM%5Bid%5D=9936786593&roleIM%5BisDisabled%5D=0&roleIM%5Bname%5D=%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%AE%A2%E6%9C%8D100%E5%8F%B7ethan%E8%BF%81%E7%A7%BB344&roleIM%5Bdata%5D=9936786593&_bqq_csrf=67c05ce90a2c7e526a3cc135ba85d42570e39873"
    # payload = f"name=%E7%BD%91%E9%A1%B5H5{channel_number}&cate=7&type=10&scene=3&sideBarId=&interactNavId=&roleIM%5BrobotNav%5D%5BrobotNavMenuSwitch%5D=0&roleIM%5Bvalue%5D=4&roleIM%5BmsgDisplayed%5D=0&roleIM%5Buin%5D=9222233975&roleIM%5Bid%5D=9222233975&roleIM%5BisDisabled%5D=0&roleIM%5Bname%5D=5.17%E6%96%B0%E5%BC%80&roleIM%5Bdata%5D=9222233975&_bqq_csrf=3d4873031c454bed629482f43a9c74a4f4a8dd82"
    payload = f"name=%E7%BD%91%E9%A1%B5H5{channel_number}&cate=7&type=10&scene=3&sideBarId=&interactNavId=&roleIM%5BrobotNav%5D%5BrobotNavMenuSwitch%5D=0&roleIM%5Bvalue%5D=4&roleIM%5BmsgDisplayed%5D=0&roleIM%5Buin%5D=9222233973&roleIM%5Bid%5D=9222233973&roleIM%5BisDisabled%5D=0&roleIM%5Bname%5D=%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%AE%A2%E6%9C%8D1%E5%8F%B70517&roleIM%5Bdata%5D=9222233973&_bqq_csrf=bb2843a1e72db4e77ba26fe171559abc48947c33"
    headers = {
        'authority': 'admin.qidian.qq.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'robot_id=922223123; __root_domain_v=.qidian.qq.com; qidian_switch_menu_first=1; pgv_pvid=3839336641; fqm_pvqid=696ca525-59f3-41af-867d-f1ff3eed6fca; fqm_sessionid=77bda485-3d59-4e15-8876-714895db006c; pgv_info=ssid=s8772649980; _qpsvr_localtk=0.6843455844687596; RK=4E0k6AmNZr; ptcz=128984f91baf1776df47c9805b0b970aa21e3b8a6db1d00fd40266e9d3663df1; tmeLoginType=2; euin=7KSFoeCzow6P; logTrackKey=3ea4df83d7324971b2178b5f08b4367a; secToken=4f64477cdc8644d3f3af94d7ffaa3da2; verifycode=HYNH; qq_domain_video_guid_verify=7ad20c9b38967c8e; Hm_lvt_3b5354c9bf27041f86175877f2134d74=1693365996; verifysession=h01a1cbd27afe040e31e6888545ad29f44ecd3609f32399bf14ff08ff005fe114789401b42c342c82d845da967f59ff2187; _qddaz=QD.895493365994593; Hm_lpvt_3b5354c9bf27041f86175877f2134d74=1693366074; qd_admin_is_web=yes; loginDomain=ac.qidian.qq.com; advanced-star4s=mhv6s8gpt0hbuek8cbhj3o0470; psrf_qqaccess_token=A02E88972305BBFF634EA0491FA953F2; psrf_access_token_expiresAt=1701743652; psrf_qqrefresh_token=F487FFB136552FDD68F3E6A0A8E8ACBF; psrf_qqunionid=3C37AB2132DFAE4F3348521C035A5444; wxrefresh_token=; wxunionid=; psrf_qqopenid=49BBF25BA141CF9C7B5852A349D4BFC9; wxopenid=; qdui_loginaccount=admin@admin05.imcc-test.qidian.qq.com; qidian_env_set=3_0; login_url=https://admin.qidian.qq.com/ac/login; ptui_loginuin=2853892641; uin=o2853892641; skey=@cEcEbd253; p_uin=o2853892641; pt4_token=ZAsebgzdHYl7MGKkUP3Ol7lZiv79oxHUqElp7IiKaUQ_; p_skey=pRLqQMV4EFVuYRls-X8LIRJpLUiJlEhvJ8XQ23bwl-4_; _bqqcsrf=416cc3afef9f4a8abee689144ac9bc2771a59688; d2=pot5wm4sGL5YC/Vs7GhG0Y63N5vfLwy+MfEdJ0W7fRTJlwjlbuI2gYPh5hux42SFsMnQCqpatjvzkjbl9ewgKZ/F2VmnO188mTGxvFyNe+cq2a+DZzTwBMB3rxCOytcs9MIeW40D3P842GiCjKNHjUByxpPM8l8NH1jOXHfOA4mqQda7GUiUSxz7fSa5u8kkum8bqX0Zw1lKY4Fd2S9TdfIwbWZyiYWJ99VJDPIlIB4+46h8gN+Pxg==; corp_uin=3009059166; aid=2853892641; aid_skey=lt0NO4mE5Bz3QH40wq+MUBRn+b9Kc7BSr8Xhp5yEpipLITmtZsfT4kURmkPpmHlAfOkcKQBKYoPWvNNBL9vEVF+qceWqKCLMMUKD+X6A/xsZvfARU0qdD1Ijc58CvfLxIhV3ESn/QI85cJRfTRiutfMqAOFb1/y22ufIKbkmov4=; login_type=qidian; source=qidian; logout_type=qidian; qd_aid_encode=f41e61cd337b4ed1e78aad6bd416b540; qidian_channel_conf=%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C10%5D; _qdda=4-1.23a990; _qddab=4-nc4qll.lm8l103k; _csrf-star4s=ca8c6f2f665de921f896bb643d842ecb46846689598ddc63efbe1e33c9d9fb19a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_csrf-star4s%22%3Bi%3A1%3Bs%3A32%3A%22O23tSLzIJ6JX7TrfdBPlQQbQ5Z3U85r8%22%3B%7D; qidian_star4s_adminbit=; qidian_current_set=10009; zhiku_robot_id=922223123; qd-zhiku=ceqciqkqkqb099mq2humfl7lsq; _csrf-frontend=0af1091512bd10e78ab3a12d2e27da644861645e9da288bd15a6eef792b13d91a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%228UHt-SF6vPwnoPZkY2xquHde5GxTtv-l%22%3B%7D; _bqq_csrf=c051371af719dd574e02836fc504d089c8ae2c8d; XSRF-TOKEN=c051371af719dd574e02836fc504d089c8ae2c8d',
        'dnt': '1',
        'origin': 'https://admin.qidian.qq.com',
        'referer': 'https://admin.qidian.qq.com/tp/wpa/single',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'c051371af719dd574e02836fc504d089c8ae2c8d'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    print(f'请求第{i}次完成')

print('请求完成')
