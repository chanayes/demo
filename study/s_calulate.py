#!/usr/bin/python3

a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

print(id(a), id(b))

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

a = 0b111100
print(a)


# -*- coding:utf-8 -*-

def NumberOf1(n):
    # write code here
    cnt = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        cnt += 1
        n = (n - 1) & n
    return cnt


class Solution:
    pass

print("\a")
