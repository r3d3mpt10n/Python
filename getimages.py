import urllib2
import re
import os
from os.path import basename
from urlparse import urlsplit
from urlparse import urlparse
from posixpath import basename,dirname

## This will be the file used to store the variables that the customer has entered. (Customer URL and Customer NAME)

from CUST_INFO import *

## These will become variables that will get their value from a javascript web box. We will be able to paste a URL into the box and it will be input into the cust_url variable section below. Likewise with the cust_name.

##CUST_URL = ""
##CUST_NAME = ""


## If there are any spaces this will replace them with '%20' ##

def process_url(CUST_URL):
    raw_url = CUST_URL
    if ' ' not in raw_url[-1]:
        raw_url=raw_url.replace(' ','%20')
        return raw_url
    elif ' ' in raw_url[-1]:
        raw_url=raw_url[:-1]
        raw_url=raw_url.replace(' ','%20')
        return raw_url
        checkDir(raw_url)

def checkDir(raw_url):
    url = raw_url
    parse_object = urlparse(url)
    dirname = basename(parse_object.path)
    if not os.path.exists('images'):
    os.mkdir("images/"+(CUST_NAME))
    os.chdir("images/"+(CUST_NAME))
    collectImg(url)

def collectImg(url):
    urlcontent = urllib2.urlopen(url).read()
    imgurls = re.findall('img .*?src="(.*?)"',urlcontent)
    for imgurl in imgurls:
        try:
            imgurl = process_url(imgurl)
            imgdata = urllib2.urlopen(imgurl).read()
            filename = basename(urlsplit(imgurl)[2])
            output = open(filename,'wb')
            output.write(imgdata)
            output.close()
            os.remove(filename)
        except:
            pass