#Webscrapping ICC Cricket Page


from bs4 import BeautifulSoup
from collections import OrderedDict
import requests
import pandas as pd


ranks = "https://www.icc-cricket.com/rankings/mens/team-rankings/t20i"
source = requests.get(ranks).text

soup = BeautifulSoup(source,"lxml")

rank_table=soup.find('table', class_='table')


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
for head in rank_table.findAll('th' , class_='table-head__cell'):
    A.append(head.text.strip())
for row in rank_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[0].text.strip())
        
        

col_data = dict(zip(A,[F,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")


