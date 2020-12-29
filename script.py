import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    list_of_file = os.listdir('files')
    if len(list_of_file) == 0:
        raise Exception("Error! No files found")
    else:
        excel_file = pd.ExcelFile('files/'+list_of_file[0])
        number_of_sheets = len(excel_file.sheet_names)
        print("File name:", list_of_file[0])
        print("Number of sheets:", number_of_sheets, "\n")
        for sheet_name in excel_file.sheet_names:
            sheet_data = pd.read_excel(excel_file, sheet_name)
            df = pd.DataFrame(sheet_data, columns = ['Time',  'Value'])
            # print(df, '\n')
            plt.plot(df['Time'], df['Value'], marker='o')
            plt.title(sheet_name)
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.grid(True)
            plt.show()

if __name__ == "__main__":
    main()