from csv import DictReader
import matplotlib
import matplotlib.dates as dates
import numpy as np
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

    def mean(self):
        return sum(self.items) / float(len(self.items))

day = []
price = []

maPrice50 = []
maPrice200 = []
fiftyPriceQueue = Queue()
twoHundredPriceQueue = Queue()

with open ('prices.csv', 'rt') as csvfile:
    data = DictReader(csvfile)
    n = 0
    for row in data:
        dateString = row['Date']
        day.append(datetime.datetime.strptime(dateString, "%Y-%m-%d"))   
        price.append(float(row['Close']))
        fiftyPriceQueue.enqueue(float(row['Close']))
        twoHundredPriceQueue.enqueue(float(row['Close']))

        if n >= 49:
            maPrice50.append(fiftyPriceQueue.mean()) 
            fiftyPriceQueue.dequeue()

        if n >= 199:
            maPrice200.append(twoHundredPriceQueue.mean())
            twoHundredPriceQueue.dequeue()

        n += 1


        





