import pandas as pd
import xlsxwriter

dataframe = pd.DataFrame({'Data' : [20, 30, 45, 12, 33, 9]})

writer = pd.ExcelWriter('simple_data.xlsx', engine='xlsxwriter')

dataframe.to_excel(writer, sheet_name='Page_1')

writer.save()