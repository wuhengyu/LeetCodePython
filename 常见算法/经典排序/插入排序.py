# -*- coding: utf-8 -*-
# @Time    : 2022/11/24 11:39
# @Author  : Walter
# @File    : 插入排序.py
# @License : (C)Copyright Walter
# @Desc    : 对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入

'''
1.选择数组第二个数为基数
2.头插入：如果小的话，暂存key这个数，依次循环交换相邻位置数值，直至j=-1不满足，跳出循环，再把key这个数等于arr[-1 + 1]，插入首位
3.中间插入：如果随着j-=1，循环至key < arr[j]不满足，跳出循环，arr[j + 1] = key，替换插入key这个数
4.数组5个数，依次外循环4次结束
'''

def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [12, 1, 8, 5, 6]
insertionSort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])