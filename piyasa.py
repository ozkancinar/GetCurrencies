#!/usr/bin/env python
__author__ = 'ozk'
import requests
from bs4 import BeautifulSoup
import time

request = requests.get("https://kur.doviz.com/serbest-piyasa/amerikan-dolari")
content = request.content
soup = BeautifulSoup(content, "html.parser")
for link in soup.findAll("div", {"class":"column-row4"}):
    link
#tek bir tagda arama yapmaz alt taglara bakar
#string_price = element.text.strip() #£139.00
#isaretsiz_deger = string_price[1:] #139.00
#tutar = float(isaretsiz_deger) #float 139.00
#print(tutar)
print("Dolar: %s"%link.text.strip())


request2 = requests.get("https://kur.doviz.com/serbest-piyasa/euro")
content2 = request2.content
soup2 = BeautifulSoup(content2, "html.parser")
for lin1 in soup2.find_all("div",{"column-row4"}):
    lin1
print("Euro: %s"%lin1.text.strip())
print("Log kaydı tutuldu")

#Dosya kayit islemleri
file = open("data.txt","a")
file.write("\nTarih: %s \n"%time.strftime("%d/%m/%Y %H:%M:%S"))
file.write("Dolar: %s \n"%link.text.strip())
file.write("Euro: %s \n"%lin1.text.strip())
file.close()
