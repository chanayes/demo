#!/usr/bin/env python3

n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print(f"1 到 {n} 之和为: {sum}")

while 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)

print("Good bye!")

count = 0
while count < 5:
    print(count, "小于 5")
    count += 1
else:
    print(count, "大于或等于 5")

# flag = 1
#
# while (flag): print('欢迎访问菜鸟教程!')
#
# print("Good bye!")

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)

word = 'runoob'

for letter in word:
    print(letter)

#  1 到 5 的所有数字：
for number in range(-2, 6):
    print(number)

for x in range(6):
    print(x)
else:
    print(f"Finally finished! {x}")

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

for i in range(0, 10, 3):
    print(i)
for i in range(-10, -100, -30):
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print(f'循环结束。{n}')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print(f'循环结束。{n}')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} 等于 {x}*{n // x}')
            break
    else:
        # 循环中没有找到元素
        print(f'{n}是质数')

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b


def fab(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


print(fab(5))
