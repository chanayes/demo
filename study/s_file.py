#!/usr/bin/python3

# 打开一个文件
f = open(r"tmp/foo.txt", "w+", encoding="utf-8")

f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")

# 关闭打开的文件
f.close()

# !/usr/bin/python3

# 打开一个文件
f = open(r"tmp/foo.txt", "r", encoding="utf-8")

str = f.read()
print(str)

# 关闭打开的文件
f.close()

# !/usr/bin/python3

# 打开一个文件
f = open("tmp/foo.txt", "r", encoding="utf-8")

str = f.readlines()
print(str)

# 关闭打开的文件
f.close()
