import json

# channel_list = ["2152-WebIM", "2153-WebIM", "2154-WebIM", "2155-WebIM", "2156-WebIM", "2157-WebIM", "2158-WebIM",
#                 "2159-WebIM", "2160-WebIM", "2161-WebIM", "2162-WebIM", "2163-WebIM", "2164-WebIM", "2165-WebIM",
#                 "2166-WebIM", "2167-WebIM", "2168-WebIM", "2169-WebIM", "2170-WebIM", "2171-WebIM", "2172-WebIM",
#                 "2173-WebIM", "2174-WebIM", "2175-WebIM", "2176-WebIM", "2177-WebIM", "2178-WebIM", "2179-WebIM",
#                 "2180-WebIM", "2181-WebIM", "2182-WebIM", "2183-WebIM", "2184-WebIM", "2185-WebIM", "2186-WebIM",
#                 "2187-WebIM", "2188-WebIM", "2189-WebIM", "2190-WebIM", "2191-WebIM", "2192-WebIM", "2193-WebIM",
#                 "2194-WebIM", "2195-WebIM", "2196-WebIM", "2197-WebIM", "2198-WebIM", "2199-WebIM", "2200-WebIM",
#                 "2201-WebIM", "2202-WebIM", "2203-WebIM", "2204-WebIM", "2205-WebIM", "2206-WebIM", "2207-WebIM",
#                 "2209-WebIM", "2210-WebIM", "2211-WebIM", "2212-WebIM", "2213-WebIM", "2214-WebIM", "2215-WebIM",
#                 "2216-WebIM", "2217-WebIM", "2218-WebIM", "2219-WebIM", "2220-WebIM", "2221-WebIM", "2222-WebIM",
#                 "2223-WebIM", "2224-WebIM", "2225-WebIM", "2226-WebIM", "2227-WebIM", "2228-WebIM", "2229-WebIM",
#                 "2230-WebIM", "2231-WebIM", "2232-WebIM", "2233-WebIM", "2234-WebIM", "2235-WebIM", "2236-WebIM",
#                 "2237-WebIM", "2238-WebIM", "2239-WebIM", "2240-WebIM", "2241-WebIM", "2242-WebIM", "2243-WebIM",
#                 "2244-WebIM", "2245-WebIM", "2246-WebIM", "2247-WebIM", "2248-WebIM", "2249-WebIM", "2250-WebIM",
#                 "2251-WebIM", "2252-WebIM", "2253-WebIM", "2254-WebIM", "2255-WebIM", "2256-WebIM", "2257-WebIM",
#                 "2258-WebIM", "2259-WebIM", "2260-WebIM", "2261-WebIM", "2262-WebIM", "2263-WebIM", "2264-WebIM",
#                 "2265-WebIM", "2266-WebIM", "2267-WebIM", "2268-WebIM", "2269-WebIM", "2270-WebIM", "2271-WebIM",
#                 "2272-WebIM", "2273-WebIM", "2274-WebIM", "2275-WebIM", "2276-WebIM", "2277-WebIM", "2278-WebIM",
#                 "2279-WebIM", "2280-WebIM", "2281-WebIM", "2282-WebIM", "2283-WebIM", "2284-WebIM", "2285-WebIM",
#                 "2286-WebIM", "2287-WebIM", "2288-WebIM", "2289-WebIM", "2290-WebIM", "2291-WebIM", "2292-WebIM",
#                 "2293-WebIM", "2294-WebIM", "2295-WebIM", "2296-WebIM", "2297-WebIM", "2298-WebIM", "2299-WebIM",
#                 "2300-WebIM", "2301-WebIM", "2302-WebIM", "2303-WebIM", "2304-WebIM", "2305-WebIM", "2306-WebIM",
#                 "2307-WebIM", "2308-WebIM", "2309-WebIM", "2310-WebIM", "2311-WebIM", "2312-WebIM", "2313-WebIM",
#                 "2314-WebIM", "2315-WebIM", "2316-WebIM", "2317-WebIM", "2318-WebIM", "2319-WebIM", "2320-WebIM",
#                 "2321-WebIM", "2322-WebIM", "2323-WebIM", "2324-WebIM", "2325-WebIM", "2326-WebIM", "2327-WebIM",
#                 "2328-WebIM", "2329-WebIM", "2330-WebIM", "2331-WebIM", "2332-WebIM", "2333-WebIM", "2334-WebIM",
#                 "2335-WebIM", "2336-WebIM", "2337-WebIM", "2338-WebIM", "2339-WebIM", "2340-WebIM", "2341-WebIM",
#                 "2342-WebIM", "2343-WebIM", "2344-WebIM", "2345-WebIM", "2346-WebIM", "2347-WebIM", "2348-WebIM",
#                 "2349-WebIM", "2350-WebIM", "2351-WebIM", "2352-WebIM", "2353-WebIM"]
# channel_list = [
#        "WeChatKeFu",
#        "2279-WebIM",
#        "2308-WebIM",
#        "2322-WebIM",
#        "2337-WebIM",
#        "2349-WebIM",
#        "2365-WebIM",
#        "2366-WebIM",
#        "2370-WebIM",
#        "2314-WebIM",
#        "2392-WebIM",
#        "2408-WebIM",
#        "2425-WebIM",
#        "2426-WebIM",
#        "2427-WebIM",
#        "2428-WebIM",
#        "2429-WebIM",
#        "2430-WebIM",
#        "2431-WebIM",
#        "2432-WebIM",
#        "2433-WebIM",
#        "2434-WebIM",
#        "2435-WebIM",
#        "2436-WebIM",
#        "2437-WebIM",
#        "2438-WebIM",
#        "2439-WebIM",
#        "2440-WebIM",
#        "2441-WebIM",
#        "2442-WebIM",
#        "2443-WebIM",
#        "2444-WebIM",
#        "2445-WebIM",
#        "2446-WebIM",
#        "2447-WebIM",
#        "2448-WebIM",
#        "2449-WebIM",
#        "2450-WebIM",
#        "2451-WebIM",
#        "2452-WebIM",
#        "2453-WebIM",
#        "2454-WebIM",
#        "2455-WebIM",
#        "2456-WebIM",
#        "2457-WebIM",
#        "2458-WebIM",
#        "2459-WebIM",
#        "2460-WebIM",
#        "2461-WebIM",
#        "2462-WebIM",
#        "2463-WebIM",
#        "2464-WebIM",
#        "2465-WebIM",
#        "2466-WebIM",
#        "2467-WebIM",
#        "2468-WebIM",
#        "2469-WebIM",
#        "2470-WebIM",
#        "2471-WebIM",
#        "2472-WebIM",
#        "2473-WebIM",
#        "2474-WebIM",
#        "2475-WebIM",
#        "2476-WebIM",
#        "2477-WebIM",
#        "2478-WebIM",
#        "2479-WebIM",
#        "2480-WebIM",
#        "2481-WebIM",
#        "2482-WebIM",
#        "2483-WebIM",
#        "2484-WebIM",
#        "2485-WebIM",
#        "2486-WebIM",
#        "2487-WebIM",
#        "2488-WebIM",
#        "2489-WebIM",
#        "2490-WebIM",
#        "2491-WebIM",
#        "2492-WebIM",
#        "2493-WebIM",
#        "2494-WebIM",
#        "2495-WebIM",
#        "2496-WebIM",
#        "2497-WebIM",
#        "2498-WebIM",
#        "2499-WebIM",
#        "2500-WebIM",
#        "2501-WebIM",
#        "2502-WebIM",
#        "2503-WebIM",
#        "2504-WebIM",
#        "2505-WebIM",
#        "2506-WebIM",
#        "2507-WebIM",
#        "2508-WebIM",
#        "2509-WebIM",
#        "2510-WebIM",
#        "2511-WebIM",
#        "2512-WebIM",
#        "2513-WebIM",
#        "2514-WebIM",
#        "2515-WebIM",
#        "2516-WebIM",
#        "2517-WebIM",
#        "2518-WebIM",
#        "2519-WebIM",
#        "2520-WebIM",
#        "2521-WebIM",
#        "2522-WebIM",
#        "2523-WebIM",
#        "2524-WebIM",
#        "2525-WebIM",
#        "2526-WebIM",
#        "2527-WebIM",
#        "2528-WebIM",
#        "2529-WebIM",
#        "2530-WebIM",
#        "2531-WebIM",
#        "2532-WebIM",
#        "2533-WebIM",
#        "2534-WebIM",
#        "2535-WebIM",
#        "2536-WebIM",
#        "2537-WebIM",
#        "2538-WebIM",
#        "2539-WebIM",
#        "2540-WebIM",
#        "2541-WebIM",
#        "2542-WebIM",
#        "2543-WebIM",
#        "2544-WebIM",
#        "2545-WebIM",
#        "2546-WebIM",
#        "2547-WebIM",
#        "2548-WebIM",
#        "2549-WebIM",
#        "2550-WebIM",
#        "2551-WebIM",
#        "2552-WebIM",
#        "2553-WebIM",
#        "2554-WebIM",
#        "2555-WebIM",
#        "2556-WebIM",
#        "2557-WebIM",
#        "2558-WebIM",
#        "2559-WebIM",
#        "2560-WebIM",
#        "2561-WebIM",
#        "2562-WebIM",
#        "2563-WebIM",
#        "2564-WebIM",
#        "2565-WebIM",
#        "2566-WebIM",
#        "2567-WebIM",
#        "2568-WebIM",
#        "2569-WebIM",
#        "2570-WebIM",
#        "2571-WebIM",
#        "2572-WebIM",
#        "2573-WebIM",
#        "2574-WebIM",
#        "2575-WebIM",
#        "2576-WebIM",
#        "2577-WebIM",
#        "2578-WebIM",
#        "2579-WebIM",
#        "2580-WebIM",
#        "2581-WebIM",
#        "2582-WebIM",
#        "2583-WebIM",
#        "2584-WebIM",
#        "2585-WebIM",
#        "2586-WebIM",
#        "2587-WebIM",
#        "2588-WebIM",
#        "2589-WebIM",
#        "2590-WebIM",
#        "2591-WebIM",
#        "2592-WebIM",
#        "2593-WebIM",
#        "2594-WebIM",
#        "2595-WebIM",
#        "2596-WebIM",
#        "2597-WebIM",
#        "2598-WebIM",
#        "2599-WebIM",
#        "2600-WebIM",
#        "2601-WebIM",
#        "2602-WebIM",
#        "2603-WebIM",
#        "2604-WebIM",
#        "2605-WebIM",
#        "2606-WebIM",
#        "2607-WebIM",
#        "2608-WebIM",
#        "2609-WebIM",
#        "2610-WebIM",
#        "2611-WebIM",
#        "2612-WebIM",
#        "2613-WebIM",
#        "2614-WebIM",
#        "2615-WebIM",
#        "2616-WebIM",
#        "2617-WebIM",
#        "2618-WebIM",
#        "2619-WebIM",
#        "2620-WebIM",
#        "2621-WebIM",
#        "2622-WebIM",
#        "2623-WebIM",
#        "MiniProgram",
#        "OfficialAccount",
#        "QQKfuin",
#        "2378-QQKfuin"
#        ]


# 线上环境
channel_list = [
       # "WeChatKeFu",
       "5415-WebIM",
       "5409-WebIM",
       "5405-WebIM",
       "5404-WebIM",
       "5401-WebIM",
       "5391-WebIM",
       "5387-WebIM",
       "5386-WebIM",
       "5384-WebIM",
       "5374-WebIM",
       "5365-WebIM",
       "5363-WebIM",
       "5359-WebIM",
       "5357-WebIM",
       "5355-WebIM",
       "5351-WebIM",
       "5341-WebIM",
       "5335-WebIM",
       "5427-WebIM",
       "5461-WebIM",
       "5468-WebIM",
       "5678-WebIM",
       "5679-WebIM",
       "5680-WebIM",
       "5681-WebIM",
       "5682-WebIM",
       "5683-WebIM",
       "5684-WebIM",
       "5685-WebIM",
       "5686-WebIM",
       "5687-WebIM",
       "5688-WebIM",
       "5689-WebIM",
       "5690-WebIM",
       "5691-WebIM",
       "5692-WebIM",
       "5693-WebIM",
       "5694-WebIM",
       "5695-WebIM",
       "5696-WebIM",
       "5697-WebIM",
       "5698-WebIM",
       "5699-WebIM",
       "5700-WebIM",
       "5701-WebIM",
       "5702-WebIM",
       "5703-WebIM",
       "5704-WebIM",
       "5705-WebIM",
       "5706-WebIM",
       "5707-WebIM",
       "5708-WebIM",
       "5709-WebIM",
       "5710-WebIM",
       "5711-WebIM",
       "5712-WebIM",
       "5713-WebIM",
       "5714-WebIM",
       "5715-WebIM",
       "5716-WebIM",
       "5717-WebIM",
       "5718-WebIM",
       "5719-WebIM",
       "5720-WebIM",
       "5721-WebIM",
       "5722-WebIM",
       "5723-WebIM",
       "5724-WebIM",
       "5725-WebIM",
       "5726-WebIM",
       "5727-WebIM",
       "5728-WebIM",
       "5729-WebIM",
       "5730-WebIM",
       "5731-WebIM",
       "5732-WebIM",
       "5733-WebIM",
       "5734-WebIM",
       "5735-WebIM",
       "5736-WebIM",
       "5737-WebIM",
       "5738-WebIM",
       "5739-WebIM",
       "5740-WebIM",
       "5741-WebIM",
       "5742-WebIM",
       "5743-WebIM",
       "5744-WebIM",
       "5745-WebIM",
       "5746-WebIM",
       "5747-WebIM",
       "5748-WebIM",
       "5749-WebIM",
       "5750-WebIM",
       "5751-WebIM",
       "5752-WebIM",
       "5753-WebIM",
       "5754-WebIM",
       "5755-WebIM",
       "5756-WebIM",
       "5757-WebIM",
       "5758-WebIM",
       "5759-WebIM",
       "5760-WebIM",
       "5761-WebIM",
       "5762-WebIM",
       "5763-WebIM",
       "5764-WebIM",
       "5765-WebIM",
       "5766-WebIM",
       "5767-WebIM",
       "5768-WebIM",
       "5769-WebIM",
       "5770-WebIM",
       "5771-WebIM",
       "5772-WebIM",
       "5773-WebIM",
       "5774-WebIM",
       "5775-WebIM",
       "5776-WebIM",
       "5777-WebIM",
       "5778-WebIM",
       "5779-WebIM",
       "5780-WebIM",
       "5781-WebIM",
       "5782-WebIM",
       "5783-WebIM",
       "5784-WebIM",
       "5785-WebIM",
       "5786-WebIM",
       "5787-WebIM",
       "5788-WebIM",
       "5789-WebIM",
       "5790-WebIM",
       "5791-WebIM",
       "5792-WebIM",
       "5793-WebIM",
       "5794-WebIM",
       "5795-WebIM",
       "5796-WebIM",
       "5797-WebIM",
       "5798-WebIM",
       "5799-WebIM",
       "5800-WebIM",
       "5801-WebIM",
       "5802-WebIM",
       "5803-WebIM",
       "5804-WebIM",
       "5805-WebIM",
       "5806-WebIM",
       "5807-WebIM",
       "5808-WebIM",
       "5809-WebIM",
       "5810-WebIM",
       "5811-WebIM",
       "5812-WebIM",
       "5813-WebIM",
       "5814-WebIM",
       "5815-WebIM",
       "5816-WebIM",
       "5817-WebIM",
       "5818-WebIM",
       "5819-WebIM",
       "5820-WebIM",
       "5821-WebIM",
       "5822-WebIM",
       "5823-WebIM",
       "5824-WebIM",
       "5825-WebIM",
       "5826-WebIM",
       "5827-WebIM",
       "5828-WebIM",
       "5829-WebIM",
       "5830-WebIM",
       "5831-WebIM",
       "5832-WebIM",
       "5833-WebIM",
       "5834-WebIM",
       "5835-WebIM",
       "5836-WebIM",
       "5837-WebIM",
       "5838-WebIM",
       "5839-WebIM",
       "5840-WebIM",
       "5841-WebIM",
       "5842-WebIM",
       "5843-WebIM",
       "5844-WebIM",
       "5845-WebIM",
       "5846-WebIM",
       "5847-WebIM",
       "5848-WebIM",
       "5849-WebIM",
       "5850-WebIM",
       "5851-WebIM",
       "5852-WebIM",
       "5853-WebIM",
       "5854-WebIM",
       "5855-WebIM",
       "5856-WebIM",
       # "5857-WebIM",
       # "5858-WebIM",
       # "5859-WebIM",
       # "5860-WebIM",
       # "5861-WebIM",
       # "5862-WebIM",
       # "5863-WebIM",
       # "5864-WebIM",
       # "5865-WebIM",
       # "5866-WebIM",
       # "5867-WebIM",
       # "5868-WebIM",
       # "5869-WebIM",
       # "5870-WebIM",
       # "5871-WebIM",
       # "5872-WebIM",
       # "5873-WebIM",
       # "5874-WebIM",
       # "5875-WebIM",
       # "5876-WebIM",
       # "5877-WebIM",
       # "5407-MiniAppPlugin",
       # "5367-MiniAppPlugin",
       # "5366-MiniAppPlugin",
       # "5347-MiniAppPlugin",
       # "5343-MiniAppPlugin",
       # "5337-MiniAppPlugin",
       # "5389-MiniAppPlugin",
       # "MiniProgram",
       # "OfficialAccount",
       # "QQKfuin"
]
json_template = {
  "Metadata": {
    "AppKey": "1676518782410952955"
  },
  "Payload": {
    "UserID": "-",
    "CategoryKey": "all",
    "FeatureID": "2_WenDaGuanLi",
    "CategoryID": "0",
    "T": 1694058680830,
    "Question": "测试问答问题1",
    "Answer": [],
    "AdvancedAnswers": [
      {
        "Type": "common",
        "Answer": "<p><a href=\"https://admin.qidian.qq.com/zhiku/robotSingle/index\" rel=\"noopener noreferrer\" target=\"_blank\" class=\"industry-rich-link\">默认答案链接</a><strong class=\"industry-rich-text\" style=\"color: rgb(230, 0, 0);\">女婿徐小宝v想</strong><img class=\"editor-emoji\" src=\"https://cdn.xiaowei.qq.com/assets/images/Expression_54.png\" data-value=\"%5B%E5%90%93%5D\" alt=\"吓\" style=\"width: 24px; min-width: 24px; height: 24px; display: inline-block;\" width=\"24\" height=\"24\"><img class=\"editor-emoji\" src=\"https://cdn.xiaowei.qq.com/assets/images/Expression_32.png\" data-value=\"%5B%E5%92%92%E9%AA%82%5D\" alt=\"咒骂\" style=\"width: 24px; min-width: 24px; height: 24px; display: inline-block;\" width=\"24\" height=\"24\"></p>"
      },
      {
        "Type": "common",
        "Answer": "分段答案1"
      },
      {
        "Type": "common",
        "Answer": "分段答案2"
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
            "Answer": "<p><strong class=\"industry-rich-text\" style=\"background-color: rgb(255, 255, 255); color: rgb(230, 0, 0);\">条件组1答案</strong><img class=\"editor-emoji\" src=\"https://cdn.xiaowei.qq.com/assets/images/Expression_35.png\" data-value=\"%5B%E6%99%95%5D\" alt=\"晕\" style=\"width: 24px; min-width: 24px; height: 24px; display: inline-block;\" width=\"24\" height=\"24\"><img class=\"editor-emoji\" src=\"https://cdn.xiaowei.qq.com/assets/images/Expression_52.png\" data-value=\"%5B%E9%98%B4%E9%99%A9%5D\" alt=\"阴险\" style=\"width: 24px; min-width: 24px; height: 24px; display: inline-block;\" width=\"24\" height=\"24\"></p>"
          }
        ],
        "RuleInfo": {
          "Type": "channel",
          "Value": [
            "5415-WebIM"
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
