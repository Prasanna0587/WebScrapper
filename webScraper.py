#LIBRARIES REQUIRED
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
data=[]
#URL of website to scrape
url="https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
#page = response.content
soup = BeautifulSoup(response.text,'html.parser')
all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
for book in all_books:
    item ={}
    item['Title'] = book.find("img").attrs["alt"]
    item['link']  = book.find("a").attrs["href"]
    item['price'] = book.find("p",class_="price_color").text[2:]
    item['stock'] = book.find("p",class_="instock availability").text.strip()
    data.append(item)
df = pd.DataFrame(data)
df.to_csv("books.csv")