#Currency Converter from Usd to Inr

import requests
#import json

url1 = "https://free.currconv.com/api/v7/convert?q="
url2 = input("Enter conversion denominations")
url3 = "&compact=ultra&apiKey=955b4a8fbc83c40bd151"
url=url1+url2+url3
response = requests.get(url)
jsonConv = response.json()

inp = int(input("Enter the value"))
print("Converted Value:" , (jsonConv[url2] * inp))


