# %% codecell
import numpy as np
import pandas as pd
import pandas_datareader as dr
from urllib.request import urlopen
from bs4 import BeautifulSoup
import seaborn as sb

import requests
import urllib.request as urllib
from datetime import datetime
import csv
# %% codecell
fecha = '20220702' ###

##########################  Expansion  #######################################
# %% codecell
url = "https://www.expansion.com/mercados.html?intcmp=MENUHOM24101&s_kw=mercados"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="mod-title normal")

article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('p', class_="")

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df1 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df1['Seccion'] ="Mercados"
df1['Fecha'] = datetime.now().date()
# %% codecell

######################### Expansion AHORRO  ################################
# %% codecell
url = "https://www.expansion.com/ahorro.html?intcmp=MENUHOM24101&s_kw=ahorro"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="ue-c-cover-content__headline")
article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('p', class_="")

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df2 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df2['Seccion'] ="Ahorro"
df2['Fecha'] = datetime.now().date()
# %% codecell

#################### Expansion EMPRESA  ###########################
# %% codecell
url = "https://www.expansion.com/empresas.html?intcmp=MENUHOM24101&s_kw=empresas"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="ue-c-cover-content__headline")
article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    # Getting the link of the article
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('p', class_="")

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        #paragraph = x[p].get_text()
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df3 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df3['Seccion'] ="Empresa"
df3['Fecha'] = datetime.now().date()
# %% codecell

#################### Expansion ECONOMIA  ###########################
# %% codecell
url = "https://www.expansion.com/economia.html?intcmp=MENUHOM24101&s_kw=economia"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="ue-c-cover-content__headline")
article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    # Getting the link of the article
    #link = coverpage_news[n].find('a')['href']
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('p', class_="")

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df4 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df4['Seccion'] ="Economia"
df4['Fecha'] = datetime.now().date()
# %% codecell
len(article_href)

#################### Expansion EMPLEO  ###########################
# %% codecell
url = "https://www.expansion.com/expansion-empleo.html?intcmp=MENUHOM24101&s_kw=exp-empleo"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="ue-c-cover-content__headline")
article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    # Getting the link of the article
    #link = coverpage_news[n].find('a')['href']
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('p', class_="")

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df5 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df5['Seccion'] ="Empleo"
df5['Fecha'] = datetime.now().date()
# %% codecell
len(article_href)

df_total = df1
df_total = df_total.append(df2)
df_total = df_total.append(df3)
df_total = df_total.append(df4)
df_total = df_total.append(df5)
len(df_total)

df_total.to_excel('expansion_'+fecha+'_total.xlsx')

# Filtering contenido relacionado con a specifit theme
from re import search
keywords='keyword1|keyword2|keyword3 key4'

df_filter_titulo = df_total[df_total['titulo'].str.contains(keywords, case=False)]
df_filter_contenido = df_total[df_total['contenido'].str.contains(keywords, case=False)]
df_filter = df_filter_titulo.append(df_filter_contenido).drop_duplicates()

# Number of articles filtered by title and content
len(df_filter)
len(df_filter_titulo)

df_filter_list = df_filter['link'].tolist()
# Export results to a csv file
df_filter.to_csv('expansion_'+fecha+'_theme.csv')
