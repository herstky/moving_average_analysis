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


class MovingAverage:
    def __init__(self, numDays):
        self.numDays = numDays
        self.priceQueue = []
        self.movingAverage = []

    def isEmpty(self):
        return self.priceQueue == []

    def enqueue(self, item):
        self.priceQueue.insert(0, item)

    def dequeue(self):
        self.priceQueue.pop()
    
    def size(self):
        return len(self.priceQueue)

    def mean(self):
        return sum(self.priceQueue) / float(len(self.priceQueue))

    def updateMA(self, iter, price):
        self.enqueue(price)
        if iter >= self.numDays - 1:
            self.movingAverage.append(self.mean())
            self.dequeue()



        

day = []
price = []

fiftyDayMA = MovingAverage(50)
twoHundredDayMA = MovingAverage(200)


with open ('prices.csv', 'rt') as csvfile:
    data = DictReader(csvfile)
    n = 0
    for row in data:
        dateString = row['Date']
        day.append(datetime.datetime.strptime(dateString, "%Y-%m-%d"))   
        price.append(float(row['Close']))

        fiftyDayMA.updateMA(n, float(row['Close']))
        twoHundredDayMA.updateMA(n, float(row['Close']))

        n += 1


        





