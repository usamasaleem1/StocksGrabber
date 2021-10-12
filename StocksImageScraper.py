import requests
from bs4 import BeautifulSoup
import os

StockName = input("Enter the stock name: ")

url = "https://www.tradingview.com/symbols/name"
url = url.replace("name", StockName)

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

img = soup.find("img", {"class": "tv-circle-logo tv-circle-logo--large tv-category-header__icon"})

img_url = img["src"]

r = requests.get(img_url)

with open(StockName + ".png", "wb") as f:
    f.write(r.content)

os.startfile(StockName + ".png")