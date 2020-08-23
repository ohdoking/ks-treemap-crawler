from bs4 import BeautifulSoup
import requests 
import os
import re
import csv
from stockHistory import StockHistory
from datetime import datetime


stockPrices = []
row =7

def getStockPrices(ticker):
	id = 1
	# til 2018.12.24
	for i in range(1, 42, 1):
		try:
			url = createBaseUrl(ticker,str(i))
			r = requests.get(url)
			soup = BeautifulSoup(r.text, 'lxml')
			items = soup.find_all('span',{'class':['p10','p11']})
			j = 0
			date = None
			price = None
			for item in items:
				# 날짜
				if (j % row) == 0:
					date = item.text
				# 시가
				if (j % row) == 3:
					price = item.text
				if date != None and price != None:	
					print(id, ticker, price, date)
					stockPrices.append(StockHistory(id, ticker, price.replace(',', ''), datetime.strptime(date, '%Y.%m.%d')))
					date = None
					price = None
					id += 1
				j += 1
		except BaseException as error:
			print('An exception occurred: {}'.format(error))

	return stockPrices

def createBaseUrl(code, page):
	baseUrl = f"https://finance.naver.com/item/sise_day.nhn?&code={code}&page={page}"
	return baseUrl

print(getStockPrices('005930'))