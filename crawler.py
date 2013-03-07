#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.request

for i in range(1,10):
	url =  'http://xkcd.com/' + str(i)
	with urllib.request.urlopen(url) as conn:
	    page = conn.read()
	soup = BeautifulSoup(page)
	print(soup.find_all('img'))
	print()
	#//*[@id="comic"]/img
