import requests

url="https://www.kaggle.com/thoolihan/los-angeles-1992-riot-deaths-from-la-times?select=la-riots-deaths.csv"
req = requests.get(url)
content = req.content

#File was coming as zip. So I couldn't finish it

