from bs4 import BeautifulSoup
import requests 
import os
import re
import csv

baseUrl = 'https://finance.naver.com/sise/entryJongmok.nhn?&page='
fileName = 'KOSPI200.csv'
kospi200Arr = []
if os.path.exists(fileName):
	os.remove(fileName)
else:
	print("sorry i can't remove {} file.".format(fileName))

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
				kospi200Arr.append(data)
				with open(fileName,'a') as f:
					writer=csv.writer(f)
					writer.writerow(data)
	except:
		pass
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