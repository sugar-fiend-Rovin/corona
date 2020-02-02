import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
from newspaper import Article
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

article = Article("https://abc7news.com/5895060/")
article.download()
article.parse()
print(article.text)

r = requests.get("https://abc7news.com/5895060/")
coverpage = r.content
s = ""
soup = BeautifulSoup(coverpage, 'html5lib')
for i in soup.find_all("html"):
	s += (i.text + " ")
print(s)
coverpage_news = soup.find_all('coronavirus')
print(coverpage_news)
coverpage_news[4].get_text()
