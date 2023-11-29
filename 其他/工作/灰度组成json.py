# -*- coding: utf-8 -*-
# Time : 2023/9/5 16:08
# Author : Walter
# File : 灰度组成json.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :

import json

channel_list = [
       "WeChatKeFu",
       "2279-WebIM",
       "2308-WebIM",
       "2322-WebIM",
       "2337-WebIM",
       "2349-WebIM",
       "2365-WebIM",
       "2366-WebIM",
       "2370-WebIM",
       "2314-WebIM",
       "2392-WebIM",
       "2408-WebIM",
       "2425-WebIM",
       "2426-WebIM",
       "2427-WebIM",
       "2428-WebIM",
       "2429-WebIM",
       "2430-WebIM",
       "2431-WebIM",
       "2432-WebIM",
       "2433-WebIM",
       "2434-WebIM",
       "2435-WebIM",
       "2436-WebIM",
       "2437-WebIM",
       "2438-WebIM",
       "2439-WebIM",
       "2440-WebIM",
       "2441-WebIM",
       "2442-WebIM",
       "2443-WebIM",
       "2444-WebIM",
       "2445-WebIM",
       "2446-WebIM",
       "2447-WebIM",
       "2448-WebIM",
       "2449-WebIM",
       "2450-WebIM",
       "2451-WebIM",
       "2452-WebIM",
       "2453-WebIM",
       "2454-WebIM",
       "2455-WebIM",
       "2456-WebIM",
       "2457-WebIM",
       "2458-WebIM",
       "2459-WebIM",
       "2460-WebIM",
       "2461-WebIM",
       "2462-WebIM",
       "2463-WebIM",
       "2464-WebIM",
       "2465-WebIM",
       "2466-WebIM",
       "2467-WebIM",
       "2468-WebIM",
       "2469-WebIM",
       "2470-WebIM",
       "2471-WebIM",
       "2472-WebIM",
       "2473-WebIM",
       "2474-WebIM",
       "2475-WebIM",
       "2476-WebIM",
       "2477-WebIM",
       "2478-WebIM",
       "2479-WebIM",
       "2480-WebIM",
       "2481-WebIM",
       "2482-WebIM",
       "2483-WebIM",
       "2484-WebIM",
       "2485-WebIM",
       "2486-WebIM",
       "2487-WebIM",
       "2488-WebIM",
       "2489-WebIM",
       "2490-WebIM",
       "2491-WebIM",
       "2492-WebIM",
       "2493-WebIM",
       "2494-WebIM",
       "2495-WebIM",
       "2496-WebIM",
       "2497-WebIM",
       "2498-WebIM",
       "2499-WebIM",
       "2500-WebIM",
       "2501-WebIM",
       "2502-WebIM",
       "2503-WebIM",
       "2504-WebIM",
       "2505-WebIM",
       "2506-WebIM",
       "2507-WebIM",
       "2508-WebIM",
       "2509-WebIM",
       "2510-WebIM",
       "2511-WebIM",
       "2512-WebIM",
       "2513-WebIM",
       "2514-WebIM",
       "2515-WebIM",
       "2516-WebIM",
       "2517-WebIM",
       "2518-WebIM",
       "2519-WebIM",
       "2520-WebIM",
       "2521-WebIM",
       "2522-WebIM",
       "2523-WebIM",
       "2524-WebIM",
       "2525-WebIM",
       "2526-WebIM",
       "2527-WebIM",
       "2528-WebIM",
       "2529-WebIM",
       "2530-WebIM",
       "2531-WebIM",
       "2532-WebIM",
       "2533-WebIM",
       "2534-WebIM",
       "2535-WebIM",
       "2536-WebIM",
       "2537-WebIM",
       "2538-WebIM",
       "2539-WebIM",
       "2540-WebIM",
       "2541-WebIM",
       "2542-WebIM",
       "2543-WebIM",
       "2544-WebIM",
       "2545-WebIM",
       "2546-WebIM",
       "2547-WebIM",
       "2548-WebIM",
       "2549-WebIM",
       "2550-WebIM",
       "2551-WebIM",
       "2552-WebIM",
       "2553-WebIM",
       "2554-WebIM",
       "2555-WebIM",
       "2556-WebIM",
       "2557-WebIM",
       "2558-WebIM",
       "2559-WebIM",
       "2560-WebIM",
       "2561-WebIM",
       "2562-WebIM",
       "2563-WebIM",
       "2564-WebIM",
       "2565-WebIM",
       "2566-WebIM",
       "2567-WebIM",
       "2568-WebIM",
       "2569-WebIM",
       "2570-WebIM",
       "2571-WebIM",
       "2572-WebIM",
       "2573-WebIM",
       "2574-WebIM",
       "2575-WebIM",
       "2576-WebIM",
       "2577-WebIM",
       "2578-WebIM",
       "2579-WebIM",
       "2580-WebIM",
       "2581-WebIM",
       "2582-WebIM",
       "2583-WebIM",
       "2584-WebIM",
       "2585-WebIM",
       "2586-WebIM",
       "2587-WebIM",
       "2588-WebIM",
       "2589-WebIM",
       "2590-WebIM",
       "2591-WebIM",
       "2592-WebIM",
       "2593-WebIM",
       "2594-WebIM",
       "2595-WebIM",
       "2596-WebIM",
       "2597-WebIM",
       "2598-WebIM",
       "2599-WebIM",
       "2600-WebIM",
       "2601-WebIM",
       "2602-WebIM",
       "2603-WebIM",
       "2604-WebIM",
       "2605-WebIM",
       "2606-WebIM",
       "2607-WebIM",
       "2608-WebIM",
       "2609-WebIM",
       "2610-WebIM",
       "2611-WebIM",
       "2612-WebIM",
       # "2613-WebIM",
       # "2614-WebIM",
       # "2615-WebIM",
       # "2616-WebIM",
       # "2617-WebIM",
       ]

# json_template = {
#     "Metadata": {
#         "AppKey": "1674038460296521625"
#     },
#     "Payload": {
#         "UserID": "-",
#         "CategoryKey": "all",
#         "FeatureID": "2_WenDaGuanLi",
#         "CategoryID": "0",
#         "T": 1693466273174,
#         "Question": "单轮问题问题1",
#         "Answer": [],
#         "AdvancedAnswers": [
#             {
#                 "Type": "common",
#                 "Answer": "<p><span style=\"background-color: rgb(255, 255, 255); color: rgba(0, 0, 0, 0.85);\">默认答案</span></p>"
#             }
#         ],
#         "EffectChannelIDs": ["all"],
#         "AnswerRules": [],
#         "Similarity": [],
#         "TagIDParent": "0",
#         "TagIDChild": "0",
#         "AssociatedQuestions": [],
#         "SimilarityQuestion": "",
#         "ValidPeriodStart": 0,
#         "ValidPeriodEnd": 0,
#         "RecommendSwitch": "on",
#         "HistoryVersions": [],
#         "GroupID": "",
#         "BlackList": [],
#         "SimilarQuestions": []
#     }
# }

json_template = {
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
}

# 遍历渠道号列表并生成200个条件组
for i, channel in enumerate(channel_list[:200]):
    channel_number = channel.split("-")[0]  # 提取渠道编号

    answer_rule = {
        "AdvancedAnswers": [
            {
                "Type": "common",
                "Answer": f"条件组{i + 1}答案"
            }
        ],
        "RuleInfo": {
            "Type": "channel",
            "Value": [channel]
        }
    }

    json_template["Payload"]["AnswerRules"].append(answer_rule)  # 将填充后的AnswerRule添加到JSON中

# 将生成的JSON数据转换为字符串格式
json_data = json.dumps(json_template, indent=2, ensure_ascii=False)

# 打印生成的JSON数据
print(json_data)
