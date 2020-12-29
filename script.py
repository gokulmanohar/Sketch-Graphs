import pandas as pd

excel_file = pd.ExcelFile('files/Data-Snapshot-(24-28-Dec-2020).xlsx')
number_of_sheets = len(excel_file.sheet_names)
# print(number_of_sheets)
for sheet_name in excel_file.sheet_names:
    sheet_data = pd.read_excel(excel_file, sheet_name)
    df = pd.DataFrame(sheet_data, columns = ['Time',  'Value'])
    print(df, '\n\n')