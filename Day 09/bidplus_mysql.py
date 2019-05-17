#BidPlus mySQL

import mysql.connector 
from selenium import webdriver
from time import sleep
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='pulkitmathur10', password='Hellheck@123',
                              host='db4free.net', database = 'bidlists')
#, database = 'forsk_test'

bids=[]
itemss=[]
quantitys=[]
addresss=[]
start_date_time=[]
end_date_time=[]
start_dates=[]
start_time=[]
end_time=[]
end_dates=[]
Z=[]

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=options)
url="https://bidplus.gem.gov.in/bidlists"

browser.get(url)

for i in range(1,11):
    path_bid='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[1]/p[1]/a'''
    try:
        bid_no=browser.find_element_by_xpath(path_bid)
    except Exception as e:
        print("[ERROR]: "+str(e))
        break
    bids.append(bid_no.text)
    
    path_items='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[1]/span'''
    items=browser.find_element_by_xpath(path_items)
    itemss.append(items.text)

    path_quantity='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[2]/span'''
    quantity=browser.find_element_by_xpath(path_quantity)
    quantitys.append(quantity.text)
    
    path_address='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[3]/p[2]'''
    address=browser.find_element_by_xpath(path_address)
    addresss.append(address.text)
    
    path_start_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[1]/span'''
    start_date=browser.find_element_by_xpath(path_start_date)
    start_date_time.append(start_date.text)
    
    path_end_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[2]/span'''
    end_date=browser.find_element_by_xpath(path_end_date)
    end_date_time.append(end_date.text)
    
    
sleep(10)
browser.quit() 

for z in range(0,len(start_date_time)):
    start_dates.append(start_date_time[z][:10])
    start_time.append(start_date_time[z][10:])
    end_dates.append(end_date_time[z][:10])
    end_time.append(end_date_time[z][10:])



# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE employee;")

# STEP 1
#c.execute("CREATE DATABASE employee;")

# STEP 2


# STEP 3
c.execute ("""CREATE TABLE bidlists12(
          bid_no TEXT,
          items INTEGER,
          quantity INTEGER,
          dept_name  TEXT
          )""")

Z = list(zip(bids,itemss,quantitys,addresss,start_date_time,end_date_time))

c.execute("SELECT * FROM bidlists12")

c.executemany("INSERT INTO bidlists12 VALUES(%s,%d,%d,%s)", Z)
conn.commit()















