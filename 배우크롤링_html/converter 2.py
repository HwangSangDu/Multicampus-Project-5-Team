

#
#
#
#

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



# with open("G-드래곤_필모리스트_2018-08-16.html", 'rt') as myfile :
#     data = myfile.read().replace("<br>", '\n')
# readHtmlElement = pd.read_html(data)
# readHtmlElement[0].to_csv("123123.csv")
# print(readHtmlElement[0])
# sys.exit()


listDir = os.listdir("/Users/adam/Desktop/1-4999_csv2")

# for item in listDir:
#     newName = item.replace(".xls", ".html")
#     os.rename(item , newName)


length = len(listDir)
# print(listDir)
# sys.exit()

listddd = []
for i in range(0 ,length):
    try :
        print(listDir[i])
        readHtmlElement = pd.read_html(listDir[i], "r")
        # print(readHtmlElement[0])
        csvDir = listDir[i].replace(".html",".csv")
        readHtmlElement[0].to_csv(csvDir)
    except:
        # with open(listDir[i], 'r') as myfile :
        #     data = myfile.read().replace("<br>", '\n')
        # readHtmlElement = pd.read_html(data)
        # csvDir = listDir[i].replace(".html",".csv")
        # readHtmlElement[0].to_csv(csvDir)
        listddd.append(listDir[i])
        continue

## print(listddd)
#
errorlist = []
for item in listddd:        
    try:
        with open(item, 'rt') as myfile :
            data = myfile.read().replace("<br>", '\n')
        readHtmlElement = pd.read_html(data)

        # readHtmlElement = pd.read_html(item)
        csvDir = item.replace(".html",".csv")
        readHtmlElement[0].to_csv(csvDir)
        print(item)
    except:
        errorlist.append(item)
        continue



errorlist2 = []
for item in errorlist:
    try:
        newItem = item.replace(".html", ".csv")
        os.rename(item, newItem)
    except:
        errorlist2.append(item)
        continue




print(errorlist2)
print(len(errorlist2))




# ## print(readHtmlElement.read())
