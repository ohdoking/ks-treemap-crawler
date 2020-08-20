from bs4 import BeautifulSoup
import requests 
import os
import re
import csv
from stock import Stock

baseUrl = 'https://finance.naver.com/sise/entryJongmok.nhn?&page='
kospi200Arr = []

def getKospi200():
	for i in range(1, 22, 1):
		try:
			url = baseUrl + str(i)
			r = requests.get(url)
			soup = BeautifulSoup(r.text, 'lxml')
			items = soup.find_all('td',{'class':'ctg'})
			
			for item in items:
				txt = item.a.get('href')
				k = re.search('[\d]+',txt)
				if k:
					code = k.group()
					name = item.text
					data = code, name
					kospi200Arr.append(Stock(code, name))
		except:
			pass

	return kospi200Arr