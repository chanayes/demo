import pandas as pd

pd.set_option('display.notebook_repr_html', False)
# 读取xls（绝对路径）
excel_file = r'C:\Users\wab\Desktop\新建 Microsoft Excel 工作表.xlsx'
df = pd.read_excel(io=excel_file, sheet_name='Sheet1')

print(df)
