# -*- coding: utf-8 -*-
# @Time    : 2022/11/25 10:29
# @Author  : Walter
# @File    : Python list 常用操作.py
# @License : (C)Copyright Walter
# @Desc    :

# 1.list 定义
li = ["a", "b", "mpilgrim", "z", "example"]
print(li)
print(li[1])

# 2.list 负数索引
li = ['a', 'b', 'mpilgrim', 'z', 'example']
print(li[-1])
print(li[-3])
print(li[1:3])
print(li[1:-1])
print(li[0:3])

# 3.list 增加元素
li = ['a', 'b', 'mpilgrim', 'z', 'example']
li.append("new")
print(li)
li.insert(2, "new")
print(li)
li.extend(["two", "elements"])
print(li)

# 4.list 搜索
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.index("example")
li.index("new")
li.index("c")
# Traceback (innermost last):
#  File "<interactive input>", line 1, in ?
# ValueError: list.index(x): x not in list
"c" in li

# 5.list 删除元素
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.remove("z")
print(li)
li.remove("new")  # 删除首次出现的一个值
print(li)  # 第二个 'new' 未删除
li.remove("c")  # list 中没有找到值, Python 会引发一个异常
# Traceback (innermost last):
#  File "<interactive input>", line 1, in ?
# ValueError: list.remove(x): x not in list
li.pop()  # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
print(li)

# 6.list 运算符
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
print(li)
li += ['two']
print(li)
li = [1, 2] * 3
print(li)

# 7.使用join链接list成为字符串
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
";".join(["%s=%s" % (k, v) for k, v in params.items()])
'server=mpilgrim;uid=sa;database=master;pwd=secret'
# join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。

# 8.list 分割字符串
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print(s)
'server=mpilgrim;uid=sa;database=master;pwd=secret'
s.split(";")
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s.split(";", 1)
['server=mpilgrim', 'uid=sa;database=master;pwd=secret']

# split 与 join 正好相反, 它将一个字符串分割成多元素 list。
# 注意, 分隔符 (";") 被完全去掉了, 它没有在返回的 list 中的任意元素中出现。
# split 接受一个可选的第二个参数, 它是要分割的次数。

# 9.list 的映射解析
li = [1, 9, 8, 4]
[elem * 2 for elem in li]
[2, 18, 16, 8]
li
[1, 9, 8, 4]
li = [elem * 2 for elem in li]
li
[2, 18, 16, 8]

# 10.dictionary 中的解析
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
params.keys()
dict_keys(['server', 'database', 'uid', 'pwd'])
params.values()
dict_values(['mpilgrim', 'master', 'sa', 'secret'])
params.items()
dict_items([('server', 'mpilgrim'), ('database', 'master'), ('uid', 'sa'), ('pwd', 'secret')])
[k for k, v in params.items()]
['server', 'database', 'uid', 'pwd']
[v for k, v in params.items()]
['mpilgrim', 'master', 'sa', 'secret']
["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'database=master', 'uid=sa', 'pwd=secret']

# 11.list 过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
[elem for elem in li if len(elem) > 1]
['mpilgrim', 'foo']
[elem for elem in li if elem != "b"]
['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
[elem for elem in li if li.count(elem) == 1]
['a', 'mpilgrim', 'foo', 'c']
