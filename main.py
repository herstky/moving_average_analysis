import dataAnalysis as da
import matplotlib.pyplot as plt




if __name__ == "__main__":
    plt.plot(da.day, da.price, label = "Prices")
    plt.plot(da.day[49::], da.maPrice50, label = "50 day MA")
    plt.plot(da.day[199::], da.maPrice200, label = "200 day MA")

    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title("Procter & Gamble")
    plt.show()