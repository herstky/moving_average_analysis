from csv import DictReader
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime 

x = []
y = []

with open ('prices.csv', 'rt') as csvfile:
    data = DictReader(csvfile)
    for row in data:
        dateString = row['Date']
        x.append(datetime.datetime.strptime(dateString, "%Y-%m-%d"))
        y.append(float(row['Close']))
        


plt.plot(x, y)
plt.show()




    