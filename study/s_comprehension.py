"""
#列表推导式

[表达式 for 变量 in 列表]
[out_exp_res for out_exp in input_list]

或者

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
"""

# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# 计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 结果值1 if 判断条件 else 结果2  for 变量名 in 原列表
list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list2)

"""
# 字典推导式
{ key_expr: value_expr for value in collection }

或

{ key_expr: value_expr for value in collection if condition }
"""
list_demo = ['Googl', 'Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
new_dict = {key: len(key) for key in list_demo}
print(new_dict)

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(dic)
print(type(dic))

"""
集合推导式

{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""
# 计算数字 1,2,3 的平方数：
setnew = {i ** 2 for i in (1, 2, 3)}
print(setnew)

# 判断不是 abc 的字母并输出：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print(type(a))

"""
元组推导式（生成器表达式）

(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
"""

# 生成一个包含数字 1~9 的元组：
a = (x for x in range(1, 10))

# 使用for循环和计数器来代替直接使用len(), 同时保留生成器的可再次遍历性
count = 0
for _ in a:
    count += 1

print("生成器对象：", a)
print("元素个数：", count)
print("对象类型：", type(a))
