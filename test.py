from csv import *
import matplotlib

with open ('prices.csv', 'rt') as csvfile:
    data = DictReader(csvfile)
    for row in data:
        print(row['Date'], row['Close'])




    