#!/usr/bin/python3


from bs4 import BeautifulSoup
import urllib.request
import os
import yaml

INFO = "INFO"
ERROR = "ERROR"
log_level = INFO

# this folder must exist at runtime
dest_folder = 'img'
alt_texts = {}

def getImages():
    os.chdir( dest_folder)

    for i in range(1,10):
        url =  'http://xkcd.com/' + str(i)
        
        with urllib.request.urlopen(url) as conn:
            page = conn.read()

        soup = BeautifulSoup(page)
        image_tags = soup.find_all('img')

        for img in image_tags:
            # img[src] is the contents of the src field
            # http://imgs.xkcd.com/comics/xxxx.png
            if 'comics' in img['src']: 
                log(INFO, 'Getting ' + img['src'])
                
                filename = ''
                if '.jpg' in  img['src']:
                    filename = str(i) + '.jpg'
                elif '.png' in img['src']:
                    filename = str(i) + '.png'
                else:
                    log(ERROR, 'Did not recognize image format: ' + img['src'])
                    break
                
                urllib.request.urlretrieve(img['src'], filename)
                alt_texts[filename] = img['title']
                break

    saveAltTexts()

def saveAltTexts():
    with open('alt.yaml', 'w') as f:
        yaml.dump(alt_texts, f)

def log(level, msg):
    if log_level == INFO:
        print(level + ': ' + msg)
    elif log_level == ERROR:
        if level == ERROR:
            print(level + ': ' + msg)

getImages()
