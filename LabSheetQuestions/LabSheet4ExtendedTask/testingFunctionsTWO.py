from WorkingWithQuandl import *
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import datetime as dt
#-------------------------------------------------------------------------------------------------------------
#Use the function to gather share data from the London Stock Exchange for three of the biggest UK
#supermarkets: Tesco, Sainsburys and Morrisons. Write you own code to compare the stock price levels and
#volatility (e.g. different averages, standard deviation) and compare with the results of commands from the
#statistics package. Use the third party package matplotlib (installed in Codio) to plot the data.
#The fourth big supermarket in the UK, Asda, is not listed as it is owned by US company Wal-Mart. You
#could try to find stock data for Wal-Mart from another of Quandl’s databases.
#--------------------------------------------------------------------------------------------------------------
#Tesco: https://www.quandl.com/data/LSE/TSCO-TESCO-share-price-TSCO-Currency-GBX


randList = list(GetFromQuandl("LSE", "TSCO"))	#Make it print a little neater
years = []
price = []
countX = 0
dateCount = 0
for i in randList:
	for j in i:
		if countX == 0:
			date = j[8:10]+"/"+j[5:7]+"/"+j[0:4]
			years.append(date)
		elif countX == 1:
			price.append(j)	
		countX +=1
	countX = 0


x = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in years]
y = range(len(x))

plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(dates.DayLocator())
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()