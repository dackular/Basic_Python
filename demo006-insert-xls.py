import xlsxwriter
import pandas as pd 

readDataframe = pd.read_excel(r'fruits.xlsx')

newDataframe = pd.DataFrame({'Name' : ['orange'], 'Price' : [88], 'Amount' : [15]})

frame = [readDataframe, newDataframe]
result = pd.concat(frame)

writer = pd.ExcelWriter('fruits.xlsx', engine='xlsxwriter')

result.to_excel(writer, index = False)
writer.save()