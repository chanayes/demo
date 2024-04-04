# -- coding: utf-8 --

import pandas as pd

file_path = r'../tmp/demo.xlsx'
df = pd.read_excel(file_path, sheet_name="Sheet1")  # sheet_name不指定时默认返回全表数据

# 打印表数据，如果数据太多，会略去中间部分
print(df)

# 打印头部数据，仅查看数据示例时常用
print(df.head())

# 打印列标题
print(df.columns)

# 打印行
print(df.index)

# 打印指定列
print(df["hp"])

# 描述数据
print(df.describe())
