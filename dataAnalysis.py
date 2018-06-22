from main import ticker
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

class BackTest:
    def __init__(self):
        self.bullishDates = []
        self.bearishDates = []
        self.tradeList = []
        self.percentChanges = []
        self.holding = False

    def movingAverageintercept(self, day, price, MA1, MA2):
        if MA2.numDays > MA1.numDays:
            self.smallMA = MA1
            self.bigMA = MA2
        else:
            self.smallMA = MA2
            self.bigMA = MA1

        if day >= self.bigMA.numDays:
            self.curSmallMA = self.smallMA.movingAverage[day - self.smallMA.numDays]
            self.curBigMA = self.bigMA.movingAverage[day - self.bigMA.numDays]
            self.prevSmallMA = self.smallMA.movingAverage[day - self.smallMA.numDays - 1]
            self.prevBigMa = self.bigMA.movingAverage[day - self.bigMA.numDays - 1]
            if self.curSmallMA > self.curBigMA and self.prevSmallMA < self.prevBigMa:
                self.bullishDates.append(row['Date'])
                self.startPrice = price
                self.holding = True
                
            if self.curSmallMA < self.curBigMA and self.prevSmallMA > self.prevBigMa:
                self.bearishDates.append(row['Date'])    
                if self.holding == True:
                    self.endPrice = price     
                    self.percentChanges.append(np.round(100 * (self.endPrice - self.startPrice) / self.startPrice, 2))
                    self.holding = False


dayList = []
priceList = []
fiftyDayMA = MovingAverage(50)
twoHundredDayMA = MovingAverage(200)
test1 = BackTest()
with open ('data\\{}.csv'.format(ticker), 'rt') as csvfile:
    data = DictReader(csvfile)
    day = 0
    for row in data:
        if row['Close'] != 'null':
            dateString = row['Date']
            price = float(row['Close'])
            dayList.append(datetime.datetime.strptime(dateString, "%Y-%m-%d"))   
            priceList.append(price)

            fiftyDayMA.updateMA(day, price)
            twoHundredDayMA.updateMA(day, price)

            test1.movingAverageintercept(day, price, fiftyDayMA, twoHundredDayMA) 

            day += 1


        





