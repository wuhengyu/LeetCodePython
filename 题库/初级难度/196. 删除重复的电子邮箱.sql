--  @Time    : 2022/11/14 14:36
--  @Author  : Walter
--  @File    : 196. 删除重复的电子邮箱.sql
--  @License : (C)Copyright Walter
--  @Desc    :
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id是该表的主键列。
该表的每一行包含一封电子邮件。电子邮件将不包含大写字母。
编写一个 SQL 删除语句来 删除 所有重复的电子邮件，只保留一个id最小的唯一电子邮件。
以 任意顺序 返回结果表。 （注意： 仅需要写删除语句，将自动对剩余结果进行查询）
'''
-- 步骤1：
SELECT p1.*
FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email
;

-- 步骤2：
SELECT p1.*
FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
;

-- 步骤3：
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

-- 1、DELETE p1
-- 在DELETE官方文档中，给出了这一用法，比如下面这个DELETE语句👇
-- DLETE t1 FROM t1 LEFT JOIN t2 ON t1.id=t2.id WHERE t2.id IS NULL;
-- 这种DELETE方式很陌生，竟然和SELETE的写法类似。它涉及到t1和t2两张表，DELETE t1表示要删除t1的一些记录，具体删哪些，就看WHERE条件，满足就删；
-- 这里删的是t1表中，跟t2匹配不上的那些记录。
-- 所以，官方sql中，DELETE p1就表示从p1表中删除满足WHERE条件的记录。
--
-- 2、p1.Id > p2.Id
-- 继续之前，先简单看一下表的连接过程，这个搞懂了，理解WHERE条件就简单了👇
-- a. 从驱动表（左表）取出N条记录；
-- b. 拿着这N条记录，依次到被驱动表（右表）查找满足WHERE条件的记录；
-- 所以，官方sql的过程就是👇
-- 先把Person表搬过来
-- a. 从表p1取出3条记录；
-- b. 拿着第1条记录去表p2查找满足WHERE的记录，代入该条件p1.Email = p2.Email AND p1.Id > p2.Id后，发现没有满足的，所以不用删掉记录1；
-- c. 记录2同理；
-- d. 拿着第3条记录去表p2查找满足WHERE的记录，发现有一条记录满足，所以要从p1删掉记录3；
-- e. 3条记录遍历完，删掉了1条记录，这个DELETE也就结束了。

