import re
from distutils.log import error
from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import json
# import pandas as pd

pagesToGet= 1
upperframe=[]  

for page in range(1, pagesToGet+1):
  # print('processing page :', page)
  url = 'https://www.politifact.com/factchecks/list/?page='+str(page)
  # print(url)

  try:
    page = requests.get(url)

  except Exception as e:
    error_type, error_obj, error_info = sys.exc_info() 
    print('error for link: ', url)
    print(error_type, 'line: ', error_info.tb_lineno)
    continue
# print(page.status_code)
# print(page.text)
# print (page.headers.get("content-type", "unknown"))

# time.sleep(2)

# print(re.findall(r'\$[0-9,.]+', page.text))

soup = BeautifulSoup(page.text, "html.parser")
frame=[]
links=soup.find_all('li',attrs={'class':'o-listicle__item'})
# print(len(links))

# links = soup.find_all("a")
# Statement = j.find("div",attrs={'class':'m-statement__quote'})

for j in links:
  Statement = j.find("div",attrs={'class':'m-statement__quote'}).text.strip()
  # print(Statement)
  Link=j.find('a')['href'].strip()
  # print(Link)
  Date = j.find('footer',attrs={'class':'m-statement__footer'}).text[-18:-1].strip()
  # print(Date)
  Source = j.find('div', attrs={'class':'m-statement__author'}).find('a').get('title').strip()
  # print(Source)
  Label = j.find('div', attrs ={'class':'m-statement__content'}).find('img',attrs={'class':'c-image__original'}).get('alt').strip()
  frame.append([Statement,Link,Date,Source,Label])
upperframe.extend(frame)

# print(frame)
json.dumps(upperframe)



# import requests
# from bs4 import BeautifulSoup
# import numpy as np

# url = "https://english.elpais.com/"

# r1 = requests.get(url)
# coverpage = r1.content

# soup1 = BeautifulSoup(coverpage, 'html5lib')

# coverpage_news = soup1.find_all('h2', class_='c_t')
# # coverpage_news[4]['href']

# number_of_articles = 5

# news_contents = []
# list_lists = []
# list_titles = []

# for n in np.arange(0, number_of_articles):
    
#     # only news articles (there are also albums and other things)
#     if "inenglish" not in coverpage_news[n].find('a')['href']:  
#         continue
    
#     # Getting the link of the article
#     link = coverpage_news[n].find('a')['href']
#     list_links.append(link)
    
#     # Getting the title
#     title = coverpage_news[n].find('a').get_text()
#     list_titles.append(title)
    
#     # Reading the content (it is divided in paragraphs)
#     article = requests.get(link)
#     article_content = article.content
#     soup_article = BeautifulSoup(article_content, 'html5lib')
#     body = soup_article.find_all('div', class_='a_c')
#     x = body[0].find_all('p')
    
#     # Unifying the paragraphs
#     list_paragraphs = []
#     for p in np.arange(0, len(x)):
#         paragraph = x[p].get_text()
#         list_paragraphs.append(paragraph)
#         final_article = " ".join(list_paragraphs)
        
#     news_contents.append(final_article)
