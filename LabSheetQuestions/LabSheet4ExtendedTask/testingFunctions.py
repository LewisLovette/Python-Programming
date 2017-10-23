from WorkingWithQuandl import *
from statistics import stdev
import matplotlib.pyplot as plt
#-------------------------------------------------------------------------------------------------------------
#Use the function to gather share data from the London Stock Exchange for three of the biggest UK
#supermarkets: Tesco, Sainsburys and Morrisons. Write you own code to compare the stock price levels and
#volatility (e.g. different averages, standard deviation) and compare with the results of commands from the
#statistics package. Use the third party package matplotlib (installed in Codio) to plot the data.
#The fourth big supermarket in the UK, Asda, is not listed as it is owned by US company Wal-Mart. You
#could try to find stock data for Wal-Mart from another of Quandl’s databases.
#--------------------------------------------------------------------------------------------------------------
#Tesco: https://www.quandl.com/data/LSE/TSCO-TESCO-share-price-TSCO-Currency-GBX

def stockQuandl(country, company):
	randList = list(GetFromQuandl(country, company))
	price = []
	countX = 0
	for i in randList:
		price.append(i[1])
		
	return(price)

def average(stock):
	average = 0
	for i in stock:
		average += int(i)

	average /= len(stock)
	average = round(average, 2)	#since it doesn't round it when I wrap it around 'len(stock'

	print("\n\n"+str(average))

	return(average)

def standardDeviation(list):
	stanDev = round(stdev(list), 2)
	print("\n\n"+str(stanDev))

	return(stanDev)

def flip(stock):
	stockFlip = list(reversed(stock))
	return(stockFlip)

tesco = stockQuandl("LSE", "TSCO")
sainsburys = stockQuandl("LSE", "SBRY")
morrisons = stockQuandl("LSE", "MRW")

#print("Tesco:\n"+str(tesco)+"\n\n\nSainsburys\n"+str(sainsburys)+"\n\n\nMorrisons:\n"+str(morrisons))
#for i in range(len(tesco)):		#range for the length tesco[]
	#print(str(i))


average(tesco)
standardDeviation(tesco)

tescoRange = len(tesco)
print("\n\n"+str(tescoRange))

plt.gca().set_color_cycle(['red', 'green', 'blue'])

plt.plot(range(len(tesco)), flip(tesco), linewidth=1.3)
plt.plot(range(len(sainsburys)), flip(sainsburys), linewidth=1.3)
plt.plot(range(len(morrisons)), flip(morrisons), linewidth=1.3)

plt.ylabel("Stock Prices (GBP)")
plt.xlabel("Time: Days (2006 - 2017)")

plt.legend(['Tesco', 'Sainsburys', 'Morrisons'], loc='upper left')
plt.title("Tesco, Sainsburys and Morrisons Stock Prices: 2006-2017")

plt.show()