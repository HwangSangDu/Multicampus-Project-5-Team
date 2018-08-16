import os
import pandas as pd
import codecs
import xlrd
import time
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import html5lib
import sys

listDir = os.listdir("/Users/adam/Desktop/csv")
length = len(listDir)

movieActorList = []
for i in range(0,length):
	f = open(listDir[i], 'r')
	reader = f.readlines()
	print(reader)
	for line in reader:
		print(line)
    	# fields = line.strip().split(',')
    	# movieActorList.append(fields[0])
 #    print(movieActorList)


f.close()