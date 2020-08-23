from bs4 import BeautifulSoup
import requests 
import os
import re
import csv
from stockHistory import StockHistory
from datetime import datetime
from getkospi200 import getKospi200

stockPrices = []
row =7
fileName = '../result/StockHistory.csv'
id = 1

def getStockPrices(ticker):
	global id
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
					data = id, ticker, price.replace(',', ''), datetime.strptime(date, '%Y.%m.%d')
					date = None
					price = None
					id += 1
					with open(fileName,'a') as f:
						writer=csv.writer(f)
						writer.writerow(data)
				j += 1
		except BaseException as error:
			print('An exception occurred: {}'.format(error))
		finally:
			temp_for_sort = []
			with open(fileName,'r') as in_file:
				for sort_line in in_file:
					temp_for_sort.append(sort_line)

			with open(fileName,'w') as out_file:
				seen = set() # set for fast O(1) amortized lookup
				for line in temp_for_sort:
					if line in seen: continue #skip duplicate

					seen.add(line)
					out_file.write(line)

def createBaseUrl(code, page):
	baseUrl = f"https://finance.naver.com/item/sise_day.nhn?&code={code}&page={page}"
	return baseUrl

def execute():
	if os.path.exists(fileName):
		os.remove(fileName)
	else:
		print("sorry i can't remove {} file.".format(fileName))

	stocks = getKospi200()
	for stock in stocks:
		print(stock.getTicker() + "ing...")
		getStockPrices(stock.getTicker())

execute()