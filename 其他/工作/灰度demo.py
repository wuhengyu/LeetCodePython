# -*- coding: utf-8 -*-
# Time : 2023/9/5 16:12
# Author : Walter
# File : 灰度demo.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :

import requests
import json

url = "https://gateway.qidian.qq.com/icr/qa/robot/qapairs/post"

payload = json.dumps({
  "Metadata": {
    "AppKey": "1658645841632776609"
  },
  "Payload": {
    "UserID": "-",
    "CategoryKey": "all",
    "FeatureID": "2_WenDaGuanLi",
    "CategoryID": "0",
    "T": 1693901474502,
    "Question": "这是一个测试问题1",
    "Answer": [],
    "AdvancedAnswers": [
      {
        "Type": "common",
        "Answer": "<p><span style=\"background-color: rgb(255, 255, 255); color: rgba(0, 0, 0, 0.85);\">默认答案</span></p>"
      },
      {
        "Type": "common",
        "Answer": "<p><span style=\"background-color: rgb(255, 255, 255); color: rgba(0, 0, 0, 0.85);\">分段答案1</span></p>"
      },
      {
        "Type": "common",
        "Answer": "<p><span style=\"color: rgba(0, 0, 0, 0.85); background-color: rgb(255, 255, 255);\">分段答案2</span></p>"
      }
    ],
    "EffectChannelIDs": [
      "all"
    ],
    "AnswerRules": [
      {
        "AdvancedAnswers": [
          {
            "Type": "common",
            "Answer": "<p><span style=\"background-color: rgb(255, 255, 255); color: rgba(0, 0, 0, 0.85);\">条件组1答案</span></p>"
          }
        ],
        "RuleInfo": {
          "Type": "channel",
          "Value": [
            "2279-WebIM"
          ]
        }
      }
    ],
    "Similarity": [],
    "TagIDParent": "0",
    "TagIDChild": "0",
    "AssociatedQuestions": [],
    "SimilarityQuestion": "",
    "ValidPeriodStart": 0,
    "ValidPeriodEnd": 0,
    "RecommendSwitch": "on",
    "HistoryVersions": [],
    "GroupID": "",
    "BlackList": [],
    "SimilarQuestions": []
  }
})
headers = {
  'authority': 'gateway.qidian.qq.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
  'content-type': 'application/json',
  'cookie': '__root_domain_v=.qidian.qq.com; qidian_switch_menu_first=1; pgv_pvid=3839336641; fqm_pvqid=696ca525-59f3-41af-867d-f1ff3eed6fca; fqm_sessionid=77bda485-3d59-4e15-8876-714895db006c; pgv_info=ssid=s8772649980; _qpsvr_localtk=0.6843455844687596; RK=4E0k6AmNZr; ptcz=128984f91baf1776df47c9805b0b970aa21e3b8a6db1d00fd40266e9d3663df1; tmeLoginType=2; euin=7KSFoeCzow6P; logTrackKey=3ea4df83d7324971b2178b5f08b4367a; secToken=4f64477cdc8644d3f3af94d7ffaa3da2; verifycode=HYNH; qq_domain_video_guid_verify=7ad20c9b38967c8e; Hm_lvt_3b5354c9bf27041f86175877f2134d74=1693365996; verifysession=h01a1cbd27afe040e31e6888545ad29f44ecd3609f32399bf14ff08ff005fe114789401b42c342c82d845da967f59ff2187; _qddaz=QD.895493365994593; Hm_lpvt_3b5354c9bf27041f86175877f2134d74=1693366074; qd_admin_is_web=yes; qidian_env_set=3_0; login_type=1; wxrefresh_token=; psrf_qqopenid=49BBF25BA141CF9C7B5852A349D4BFC9; wxopenid=; wxunionid=; psrf_qqunionid=3C37AB2132DFAE4F3348521C035A5444; psrf_qqrefresh_token=B2A8DD98DD7BF018DA4AC4ED2383E897; psrf_access_token_expiresAt=1701572364; psrf_qqaccess_token=5FDB6130967761EBF77F66E89942FAB6; loginDomain=ac.qidian.qq.com; login_url=https://admin.qidian.qq.com/ac/login; ptui_loginuin=2885528484; uin=o2885528484; skey=@E5lf4Lk4V; p_uin=o2885528484; pt4_token=x8YEUexWDYBRzj5LRP-paZGCyVW45fbzU6gRQSrY4Bs_; p_skey=eqpnwkHoTHgPtuS1R7Yxju48WNoGpZ2izzarAR2PMik_; _bqqcsrf=334aa830371f4c33fefed2f82c57fd963d20d391; d2=1C/eaz/byVmWwK4c14gWQ+uiIzU5GjiAuWU0zn+k3+aWSvJ2fWugGGiOTlxPScvoNNZyU/IjDy8S/zf//pycHVWHpzsPfJtiVVeWJYIuS2u45tVF59bbdnKo2yGlwR85pI15tnfiE/CrxjunLbkshsvhNPKEq4oEMvYbJnmV4tXMjg35BTwjm00nKmODVwFCSZQuCbP8BLXW4Rkn0biCWGljP3eNm15qYkbjo+nBqiphqIDC+Ojf7g==; corp_uin=3009126925; aid=2885528484; aid_skey=ktD+vdJjA/GLKOujrWo7loFOF3Vyfkf7oHm0C6mcJlD1NjfqePV6piemV6tm64NzpZSPM70VshvE8fPLGU1L15B3FHt2Elnfgj5YofgLPd3K4mahNsnHvWfO3p2k6gfq3P650uB9nlrwR3NJS7GRjC1Q3yYJgm/M1tRzbzfB6tw=; login_type=1; source=1; logout_type=1; qd_aid_encode=19589cf73b75d465359bed3a4d6d9061; _bqq_csrf=70083f6e195acd53169c7df93a3ed09bb8672e82; XSRF-TOKEN=70083f6e195acd53169c7df93a3ed09bb8672e82',
  'dnt': '1',
  'origin': 'https://xiaowei.qidian.qq.com',
  'referer': 'https://xiaowei.qidian.qq.com/',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest',
  'x-timestamp': '1693901475',
  'x-xsrf-token': '70083f6e195acd53169c7df93a3ed09bb8672e82',
  'yxw-accounttype': 'qidian',
  'yxw-secretid': 'e1a3eae44d1ba905ce442d9abd570590'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
