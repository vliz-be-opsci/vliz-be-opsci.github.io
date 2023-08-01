import requests
import time
from bs4 import BeautifulSoup
import json
import os
import yaml

def author_name_finder(author_name, text):
    # Split the author name into a list of words and check if the last word is found in text
    tofind = author_name.split(" ")[-1]
    if tofind in text:
        return True
    else:
        return False

def scrape_articles(author_name, min_year, max_year=None):
    articles = []
    url = f"https://scholar.google.be/scholar?q={author_name}&hl=nl&as_sdt=0%2C5&as_ylo={min_year}&as_yhi={max_year}"
    start = 0
    while url:
        start += 10
        author_found = False
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        for article in soup.select('.gs_scl'):
            try:
                title = article.select_one('.gs_rt').text
                authors = article.select_one('.gs_a').text
                text = article.select_one('.gs_rs').text
                
                #remove all non utf-8 characters and \n and \t from the title, authors and text
                title = title.encode('ascii', 'ignore').decode('ascii')
                text = text.encode('ascii', 'ignore').decode('ascii')
                authors = authors.encode('ascii', 'ignore').decode('ascii')
                
                #extract year from authors
                parts = authors.split(",")[-1].split("-")
                #find YYYY in parts
                for part in parts:
                    part = part.strip()
                    if len(part) == 4:
                        #check if int(part) is a year
                        if max_year == None:
                            max_year_test = 9999999
                        if int(part) >= min_year and int(part) <= max_year_test:
                            year = int(part)
                            break
                if author_name_finder(author_name, authors):
                    author_found = True
                    articles.append({
                        'title': title,
                        'authors': authors,
                        'text': text,
                        'year': year
                    })
            except Exception as e:
                print(e)
        if start > 100:
            return articles
        if author_found:
            url = f"https://scholar.google.be/scholar?start={start}&q={author_name}&hl=nl&as_sdt=0%2C5&as_ylo={min_year}&as_yhi={max_year}"
            time.sleep(10)
        else: 
            return articles

#articles = scrape_articles('Katrina Exter', 2018)
#pretty_print(articles)
#print(json.dumps(articles, indent=4))

#load in ../data/open-science-team/members.yml
#loop over all members
#scrape articles for each member

#get parent directory
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"_data","open-science-team","members.yml")) as f:
    members = yaml.load(f, Loader=yaml.FullLoader)

all_articles = []
for member in members:
    name = member['name']
    print(f"Scraping articles for {name}")
    articles_author = scrape_articles(name, 2018)
    for article in articles_author:
        #check if article is already in all_articles by checking the title
        title = article['title']
        title_found = False
        for article_all in all_articles:
            if article_all['title'] == title:
                title_found = True
                break
        if not title_found:
            all_articles.append(article)
print(json.dumps(all_articles, indent=4))
print(f"Found {len(all_articles)} articles")

    