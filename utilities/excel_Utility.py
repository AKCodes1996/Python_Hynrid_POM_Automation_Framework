
'''
from openpyxl import load_workbook

workbook = load_workbook(r"F:\Test_proj\DataSet\Cred.xlsx")
sheet = workbook["Sheet1"]
sheet = workbook.active
print(sheet["A2"].value)
'''

import pandas as pd

def read_data_as_list():
    df = pd.read_excel(r"F:\Test_proj\DataSet\Cred.xlsx")
    products = df["Product"].tolist()
    return products