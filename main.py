from dataAnalysis import *
import matplotlib.pyplot as plt

ticker = "CMG"

if __name__ == "__main__":
    plt.plot(dayList, priceList, label = "Prices")
    plt.plot(dayList[fiftyDayMA.numDays - 1::], fiftyDayMA.movingAverage, label = "50 day MA")
    plt.plot(dayList[twoHundredDayMA.numDays - 1::], twoHundredDayMA.movingAverage, label = "200 day MA")

    print('bullish: {}'.format(test1.bullishDates))
    print('bearish: {}'.format(test1.bearishDates))
    print('returns: {}'.format(test1.returns))
    print('algorithm return: {}%'.format(np.round(np.sum(test1.returns), 2)))
    print('total return: {}%'.format(np.round(100 * (priceList[-1] - priceList[0]) / priceList[0], 2)))


    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title("{} Prices".format(ticker))
    plt.show()

    