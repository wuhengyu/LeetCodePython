# -*- coding: utf-8 -*-
# Time : 2023/12/6 22:05
# Author : Walter
# File : 协程测试.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :

import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(80)  # 暂停1秒钟
    print("Task 1: Resume")
    await asyncio.sleep(1)  # 暂停1秒钟
    print("Task 1: End")

async def task2():
    print("Task 2: Start")
    await asyncio.sleep(90)  # 创建一个异步点，让事件循环可以切换到其他任务
    print("Task 2: Resume")
    await asyncio.sleep(0)  # 创建另一个异步点
    print("Task 2: End")

async def main():
    print("Main: Start")
    await asyncio.gather(task1(), task2())  # 同时运行 task1 和 task2
    print("Main: End")

asyncio.run(main())