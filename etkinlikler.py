import requests
from bs4 import BeautifulSoup
import time
import re

request = requests.get("https://etkinlik.sdu.edu.tr/EtkinlikListesi.aspx")
content = request.content
soup = BeautifulSoup(content, "html.parser")
for link in soup.findAll('tr',{"class":"rlvI"}):
    link
i=0
metin = []
for abc in soup.findAll('tbody'):
    print(abc.text.strip("\n"))
    i = i+1
    print(i)
    #metin.append(str(abc.text.strip().strip("\n")))
al = abc.text.strip()
metin = al.strip("\n")
#print(metin)
element = soup.find('tbody')
son = ""

filtered = filter(lambda x:  not re.match(r'^\s*$', x), str(metin))
print(str(filtered))