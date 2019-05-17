#ICC Ranks SQLite

from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd


ranks = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(ranks).text

soup = BeautifulSoup(source,"lxml")

rank_table=soup.find('table', class_='table')


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in rank_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[0].text.strip())
        
        

conn = sqlite3.connect ( 'iccrank.db' )

c = conn.cursor()
c.execute ("""CREATE TABLE rank_odi1(
          Pos INTEGER,
          Team  TEXT,
          Weighted_Matches INTEGER,
          Points INTEGER,
          Rating INTEGER
          )""")


A = list(zip(F,B,C,D,E))


c.execute("SELECT * FROM rank_odi1")
with conn:
    c.executemany("INSERT INTO rank_odi1(Pos,Team, Weighted_Matches, Points, Rating) VALUES(?,?,?,?,?)", A)

c.execute("SELECT * FROM rank_odi1")
df_rank = pd.DataFrame(c.fetchall())
df_rank.columns=["Pos","Team","Weighted_Matches","Points","Rating"]

conn.close()
          
          
          
          
          
          
          
          
          