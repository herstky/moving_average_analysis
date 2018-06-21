import dataAnalysis as da
import matplotlib.pyplot as plt




if __name__ == "__main__":
    plt.plot(da.day, da.price)
    plt.plot(da.day[49::], da.maPrice50)
    plt.plot(da.day[199::], da.maPrice200)
    
    plt.show()