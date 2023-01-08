import requests

city=input("ENTER THE CITY NAME:")

url="http://api.openweathermap.org/data/2.5/weather?q={city)&appid-(API key)"

data=requests.get(url).json()
print(data)