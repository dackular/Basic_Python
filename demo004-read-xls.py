import pandas as pd

dataframe = pd.read_excel(r'fruits.xlsx')
print(dataframe)

#print("Print Name Only")
print(dataframe['Name'])
print(dataframe['Price'])
