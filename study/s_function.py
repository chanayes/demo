#!/usr/bin/python3

# 可写函数说明
def printme(str='www'):
    print(str)
    return


# 调用printme函数
printme()


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)


# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(10, 20, 30, d=40, e=50, f=60)
f(10, 20, c=30, d=40, e=50, f=60)
f(10, 20, 30, 40, e=50, f=60)


# 可写函数说明
def printinfo(age, name=2):  # 默认参数不在最后，会报错
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


printinfo(10)
