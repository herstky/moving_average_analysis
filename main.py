from dataAnalysis import *
import matplotlib.pyplot as plt




if __name__ == "__main__":
    plt.plot(dayList, priceList, label = "Prices")
    plt.plot(dayList[fiftyDayMA.numDays - 1::], fiftyDayMA.movingAverage, label = "50 day MA")
    plt.plot(dayList[twoHundredDayMA.numDays - 1::], twoHundredDayMA.movingAverage, label = "200 day MA")

    print('bullish: {}'.format(test1.bullishDates))
    print('bearish: {}'.format(test1.bearishDates))
    print('percent changes: {}'.format(test1.percentChanges))
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title("Procter & Gamble")
    plt.show()

    