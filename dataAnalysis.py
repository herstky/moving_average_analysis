from csv import DictReader
import matplotlib
import matplotlib.dates as dates
import datetime 

#implementation of queue, used for moving average calculations
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()
    
    def size(self):
        return len(self.items)

x = []
y = []

with open ('prices.csv', 'rt') as csvfile:
    data = DictReader(csvfile)
    day = 0
    for row in data:
        dateString = row['Date']
        x.append(datetime.datetime.strptime(dateString, "%Y-%m-%d"))   
        y.append(float(row['Close']))
        if day > 19:
            print(row['Date'], row['Close'])
        day += 1


        





