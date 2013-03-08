#!/usr/bin/python3


from bs4 import BeautifulSoup
import urllib.request
import os

INFO = "INFO"
ERROR = "ERROR"
log_level = INFO

dest_folder = 'img'

def getImages():
	print (os.getcwd()) # todo remove
	os.chdir( dest_folder)

	for i in range(1,10):
		url =  'http://xkcd.com/' + str(i)
		
		with urllib.request.urlopen(url) as conn:
			page = conn.read()

		soup = BeautifulSoup(page)
		image_tags = soup.find_all('img')

		for img in image_tags:
			if 'comics' in img['src']: # img[src] is the contents of the src field
				log(INFO, 'Getting ' + img['src'])
				if '.jpg' in  img['src']:
					urllib.request.urlretrieve(img['src'], str(i) + '.jpg')
					break
				elif '.png' in img['src']:
					urllib.request.urlretrieve(img['src'], str(i) + '.png')
					break
				else:
					log(ERROR, 'Did not recognize image format: ' + img['src'])



def log(level, msg):
	if log_level == INFO:
		print(level + ': ' + msg)
	elif log_level == ERROR:
		if level == ERROR:
			print(level + ': ' + msg)

getImages()
