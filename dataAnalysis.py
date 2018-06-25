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

#trade algorithm classes should inherit from this class
class Trade:
    def __init__(self):
        self.bullishDates = []
        self.bearishDates = []
        self.tradeList = []
        self.returns = []
        self.holding = False

    def buy(self, day, price):
        self.startPrice = price
        self.holding = True
        self.bullishDates.append(row['Date'])
    
    #if percent < 100 holding should be True until all shares "held" are sold
    #sum of percent should not exceed 100 
    def sell(self, day, price, percent=100, holding=False):
        self.bearishDates.append(row['Date'])    
        if self.holding == True:   
            self.returns.append(np.round(100 * (price - self.startPrice) / self.startPrice, 2))
            self.holding = False


class MAAlgorithm(Trade):
    def movingAverageIntercept(self, day, price, MA1, MA2):
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
                self.buy(day, price)
                
            if self.curSmallMA < self.curBigMA and self.prevSmallMA > self.prevBigMa:
                self.sell(day, price)
    

dayList = []
priceList = []
fiftyDay = MovingAverage(50)
twoHundredDay = MovingAverage(200)
test1 = MAAlgorithm()
with open ('data\\{}.csv'.format(ticker), 'rt') as csvfile:
    data = DictReader(csvfile)
    day = 0
    for row in data:
        if row['Close'] != 'null':
            dateString = row['Date']
            price = float(row['Close'])
            dayList.append(datetime.datetime.strptime(dateString, "%Y-%m-%d"))   
            priceList.append(price)

            fiftyDay.updateMA(day, price)
            twoHundredDay.updateMA(day, price)

            test1.movingAverageIntercept(day, price, fiftyDay, twoHundredDay) 

            day += 1


        





