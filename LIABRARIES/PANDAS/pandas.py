import pandas as pd
import matplotlib.pyplot as plt

df=pd.ExcelFile("C:\\Users\\My Lappie\\PycharmProjects\\marks.xlsx")
#check the names of  sheets in excel file
print(df.sheet_names)
#many functions do not work with ExcelFile() so use read_excel()
df1=pd.read_excel("C:\\Users\\My Lappie\\PycharmProjects\\marks.xlsx",0)
print(df1.dtypes)#Return the dtypes in df1 object.
print(df1.axes)#Return a list with the row axis labels and column axis labels
print(df1.ndim)#Number of axes / array dimensions
print('Shape=',df1.shape)
print('No of elements:',df1.size)
print(df1.head(10))
#retrieving data based on integer based indexing for position
print(df1.iloc[5])
print(df1.loc[0:5,'Name of Student'])
print(df1['Name of Student'])
#using plot function of pandas
df1.plot(x='Name of Student',y='Marks Obt.',title='Marks Data', figsize=(10,5),kind='bar')
# standard deviation of the specific column Marks Obt.
SD=df1.loc[:,"Marks Obt."].std()
print("Std. Deviation=",SD)
Mean=df1.loc[:,"Marks Obt."].mean()
print('Mean=',Mean)
