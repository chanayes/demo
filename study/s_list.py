#!/usr/bin/python3

list = ['abcd', 786, 2.23, 'runoob', 70.2]  # 定义一个列表
tiny_list = [123, 'runoob']

print(list)  # 打印整个列表
print(list[0])  # 打印列表的第一个元素
print(list[1:3])  # 打印列表第二到第三个元素（不包含第三个元素）
print(list[2:])  # 打印列表从第三个元素开始到末尾
print(tiny_list * 2)  # 打印tinylist列表两次
print(list + tiny_list)  # 打印两个列表拼接在一起的结果


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

list = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a, b))
print("operator.eq(c,b): ", operator.eq(c, b))

dd = set()
tup1 = ()

dd = ('Hi!', 'ddd') * 4
print(dd)

for x in (1, 2, 3):
    print(x, end=" ")

