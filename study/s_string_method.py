print('hello'.capitalize())

print("str.center(20, '*') : ", "[runoob]".center(20, '*'))

str = "www.runoob.com"
sub = 'o'
print("str.count('o') : ", str.count(sub))

sub = 'run'
print("str.count('run', 0, 10) : ", str.count(sub, 0, 10))

str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

Str = 'Runoob example....wow!!!'
suffix = '!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 10))
suffix = 'run'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 10))

str = "runoob\t12345\tabc"
print('原始字符串:', str)
# 默认 8 个空格
# runnob 有 6 个字符，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，后面的 \t 填充 3 个空格
print(r'替换 \t 符号:', str.expandtabs())

str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.find(str2))
print(str1.find(str2, 5))
print(str1.find(str2, 10, 20))

str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.index(str2))
print(str1.index(str2, 5))
# print(str1.index(str2, 10))

print('www.example.com'.lstrip('cmowz.'))
print('ccc.example.com'.lstrip('cmowz.'))
print('mm.example.com'.lstrip('cmowz.'))
print('woo.example.com'.lstrip('cmowz.'))
print('wzc.example.com'.lstrip('cmowz.'))

# 字母 R 替换为 N
txt = "Runoob!"
mytable = txt.maketrans("R", "N")
print(txt.translate(mytable))

# 使用字符串设置要替换的字符，一一对应
trantab = str.maketrans("aeiou", "12345")
str = "this is string example....wow!!!"
print(str.translate(trantab))

txt = "Google Runoob Taobao!"
x = "mSa"
y = "eJo"
z = "odnght"  # 设置删除的字符
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))

n = input("")
s = "〇一二三四五六七八九"
for c in "0123456789":
    n = n.replace(c, s[eval(c)])
print(n)

url = "http://www.baidu.com/python/image/123456.jpg"
# 以“.” 进行分隔
path = url.split(".")
print(path)
path = url.split("/")[-1]
print(path)

str = "123abcrunoob31221"
print(str.strip('12'))  # 字符序列为 12

import re

# 使用 input_str 替代 str 作为变量名，避免覆盖内置类型
input_str = "123abcrunoob31221"

# 移除了多余的 flags=re.M，因为这里的正则表达式不需要它
result = re.sub(r'^12|12$', '', input_str)

# 输出结果
print(result)  # 输出: "3abcrunoob31221"

import re


def remove_prefix_suffix(input_str, pattern):
    """
    从输入字符串中移除开头和结尾匹配给定模式的字符串。

    :param input_str: 需要处理的字符串
    :param pattern: 需要移除的模式字符串
    :return: 移除开头和结尾模式后的字符串
    """
    # 验证输入
    if not isinstance(input_str, str) or not isinstance(pattern, str):
        raise ValueError("input_str 和 pattern 必须是字符串类型")

    # 使用 re.sub 移除指定模式
    # re.M 标志在这里不是必须的，因为它主要用于多行模式匹配，而我们不需要这个功能
    result = re.sub(r'^{}|{}$'.format(re.escape(pattern), re.escape(pattern)), '', input_str)

    return result


# 测试函数
input_str = "123abcrunoob31221"
pattern_to_remove = "12"
result = remove_prefix_suffix(input_str, pattern_to_remove)

# 输出结果
print(result)  # 输出: "3abcrunoob31221"

