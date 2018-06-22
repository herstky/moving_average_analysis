from csv import DictReader
import matplotlib
import matplotlib.dates as dates
import numpy as np
import datetime 

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

   
    def updateMA(self, day, price):
        self.enqueue(price)
        if day >= self.numDays - 1:
            self.movingAverage.append(self.mean())
            self.dequeue()
      
dayList = []
priceList = []

fiftyDayMA = MovingAverage(50)
twoHundredDayMA = MovingAverage(200)

with open ('prices.csv', 'rt') as csvfile:
    data = DictReader(csvfile)
    day = 0
    for row in data:
        dateString = row['Date']
        price = float(row['Close'])
        dayList.append(datetime.datetime.strptime(dateString, "%Y-%m-%d"))   
        priceList.append(price)

        fiftyDayMA.updateMA(day, price)
        twoHundredDayMA.updateMA(day, price)

        day += 1


        





