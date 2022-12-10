# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 22:54
# @Author  : Walter
# @File    : dict() 函数.py
# @License : (C)Copyright Walter
# @Desc    : dict() 函数用于创建一个字典。
'''
参数：
**kwargs -- 关键字。
mapping -- 元素的容器，映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
iterable -- 可迭代对象。
返回值:
返回一个字典。
'''

# 创建空字典
print(dict())
# 传入关键字
print(dict(a='a', b='b', t='t'))
# 映射函数方式来构造字典
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
# 可迭代对象方式来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)]))

# 只使用关键字参数创建字典
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))
empty = dict()
print('empty =', empty)
print(type(empty))

# 使用可迭代对象创建字典
# 没有设置关键字参数
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =', numbers1)
# 设置关键字参数
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =', numbers2)
# zip() 创建可迭代对象
numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print('numbers3 =', numbers3)


# 使用映射来创建字典
# 映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =', numbers1)
# 以下代码不需要使用 dict()
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =', numbers2)
# 关键字参数会被传递
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =', numbers3)