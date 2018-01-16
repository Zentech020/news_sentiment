from bs4 import BeautifulSoup
import requests
import time
from random import randint
import csv
from textblob import TextBlob
import pandas as pd


def scrape_news_summaries(s):
    time.sleep(randint(0, 2))  # relax and don't let google be angry
    r = requests.get("https://news.google.com/news/")
    print(r.status_code)  # Print the status code
    content = r.text
    news_summaries = []
    soup = BeautifulSoup(content, "html.parser")
    st_divs = soup.findAll("a", {"class": "nuEeue"})
    for st_div in st_divs:
        news_summaries.append(st_div.text)
    return news_summaries


l = scrape_news_summaries("T-Notes")

for n in l:
    print("\n" + n)

a = []
for text in l:
    analysis = TextBlob(text)
    # print(analysis.sentiment.polarity)
    a.append(analysis.sentiment.polarity)
    # print("")

s = pd.Series(a)
data = s[s.nonzero()[0]]
print(data.std())