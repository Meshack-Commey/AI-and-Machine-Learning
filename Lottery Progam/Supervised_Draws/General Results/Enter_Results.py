import numpy as np
import pandas as pd
import datetime


data = list(input("Enter Ticket with NO spaces: "))
Row = int(input("Row number: "))
#Date = datetime.datetime(day, month,year)

print("my ticket: {}".format(data))

df = pd.DataFrame([data], index=[Row],columns=['1st Ball','2nd Ball','3rd Ball','4th Ball','5th Ball'])

print(df)

'''
with open("General_Results.csv","w+") as file:
	file.write(df)


with open("General_Results.csv","r+") as file:
	read= file.read()
	print(read)
'''




