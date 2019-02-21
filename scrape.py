from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import time

source = requests.get('http://ukpollingreport.co.uk').text

soup = BeautifulSoup(source, 'lxml')

table = soup.table

table_rows = table.find_all('tr')
c = []
x = [] #dates of poll
y = [] #conservatives
z = [] #Labour
a = [] #Lib Dems


for tr in table_rows:
    td = tr.find_all('td')
    row= [i.text for i in td]
    x.append(row[1]) #dates
    y.append(row[2]) #con
    z.append(row[3]) #lab
    a.append(row[4]) #lib
    c.append(+1)
    # print(con,lab,lib)


# print(a,y,z)
plt.legend(["conservatives", "Labour", "Lib Dems"])
plt.axis([0,10,0,40])
plt.plot(y,'ro')
plt.plot(z, 'bs')
plt.plot(a,'g^')
plt.show()