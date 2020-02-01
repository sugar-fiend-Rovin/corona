import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.cnn.com/us/live-news/kobe-bryant-dies-in-helicopter-crash/index.html")
coverpage = r.content

soup = BeautifulSoup(coverpage, 'html5lib')

coverpage_news = soup.find_all('h')
coverpage_news[4].get_text()
