# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:10
# Author  : Walter
# File    : Dijkstra算法.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    : 迪克斯特拉算法
'''
Dijkstra算法是一种用于找到带权图的单源最短路径的贪心算法。它的基本思想是从起点开始，
对所有节点进行标记，然后计算从起点到每个节点的最短路径，最后选择路径最短的节点作为下一个处理的节点，
并重复此过程直到到达目标节点或者处理完所有节点。
'''
'''
代码说明：
首先，我们定义一个函数(dijkstra)来实现Dijkstra算法。该函数接受一个带权有向图(graph)和一个起始节点(start)作为输入，并返回一个字典(distances)，其中每个节点都对应着从起始节点到该节点的最短距离。
在该函数中，我们首先初始化所有节点的距离为正无穷大，并将起始节点的距离设置为0。然后，我们使用一个堆(heapq)来存储所有待处理的节点，并按照它们到起始节点的距离进行排序。
在每次迭代中，我们从堆(heapq)中取出距离起始节点最近的节点(node)，并将它的距离(dist)与当前已知的距离(distances)进行比较。如果它的距离大于等于当前已知的距离，则说明它已经被处理过了，我们可以忽略它。否则，我们更新它的距离(distances)并将它的所有邻居添加到堆(heapq)中。
在循环结束后，我们将最终的距离(distances)返回。
最后，我们使用一个示例图(graph)和一个起始节点(start)来测试该函数，并将最短距离(distances)打印出来。
输出结果为：
{'A': 0, 'B': 1, 'C': 4, 'D': 4, 'E': 3, 'F': 9, 'G': 5}
该结果表明，从起始节点(A)到每个节点的最短距离分别为0、1、4、4、3、9和5。
'''
import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        (dist, node) = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return distances


# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3, 'E': 2},
    'C': {'F': 5},
    'D': {'G': 1},
    'E': {'G': 4},
    'F': {'G': 2},
    'G': {}
}
start = 'A'
distances = dijkstra(graph, start)
print(distances)
