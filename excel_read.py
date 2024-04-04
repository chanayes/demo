import pandas as pd

# 设置pandas选项
pd.set_option('display.notebook_repr_html', False)


def read_excel_file(file_path, sheet_name='Sheet1'):
    """
    读取并返回Excel文件指定表单的数据。

    参数:
    - file_path: str, Excel文件的路径。
    - sheet_name: str, 要读取的表单名称，默认为'Sheet1'。

    返回:
    - df: pandas DataFrame, 从Excel表单中读取的数据。
    """
    try:
        # 使用pandas读取Excel表单数据
        return pd.read_excel(io=file_path, sheet_name=sheet_name)
    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到。")
        return None
    except PermissionError:
        print(f"没有足够的权限读取文件 '{file_path}'。")
        return None
    except Exception as e:
        print(f"读取文件 '{file_path}' 时发生错误: {e}")
        return None


# 使用相对路径读取Excel文件
excel_file = r'C:\Users\wab\Desktop\新建 Microsoft Excel 工作表.xlsx'
df = read_excel_file(excel_file)

# 如果成功读取数据，打印数据帧
if df is not None:
    print(df)
