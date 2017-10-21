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

def stockQuandl(country, company):
	randList = list(GetFromQuandl(country, company))	#Make it print a little neater
	price = []
	countX = 0
	for i in randList:
		price.append(i[1])
		
	return(price)

tesco = stockQuandl("LSE", "TSCO")
sainsburys = stockQuandl("LSE", "SBRY")
morrisons = stockQuandl("LSE", "MRW")
averages = []

for i in range(len(tesco)):		#range for the length tesco[]
	#print(str(i))