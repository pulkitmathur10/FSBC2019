#JSON Parser

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Bhilwara"
url3 = "&appid=c0e12bb38186d2e8f365845e50f7fe8e"

url = url1 + url2 + url3

response = requests.get(url)
jsonResp = response.json()

print("Longitude:" ,jsonResp['coord']['lon'])
print("Latitude: " ,jsonResp['coord']['lat'])
print("Wind Speed: " ,jsonResp['wind']['speed'])
print("Temperature: " ,(jsonResp['main']['temp'] -273))
print("Weather Conditions:" ,jsonResp['weather'][0]['main'])
print("Sunrise: ",jsonResp['sys']['sunrise'])
print("Sunset: ",jsonResp['sys']['sunset'])

