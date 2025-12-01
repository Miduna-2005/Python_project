import pandas as pd

#df = pd.read_csv('StudentsPerformance.csv')
#df.to_csv('StudentsPerformance.csv', index=False)
#df = pd.read_csv('StudentsPerformance.csv')
#print(df)
import datetime

filename=input("Enter filename to read (e.g. data.csv): ")
file_obj=None
try:
    file_obj = open(filename, 'r')
    #content=file_obj.read()
    df=pd.read_csv(file_obj)
    print(df)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")