#!/usr/local/bin/python3

import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.bbc.co.uk/news')
doc = BeautifulSoup(response.text, 'html.parser')


stories = doc.find_all('div', { 'class': 'gs-c-promo' })
for story in stories:
    headline = story.find('h3')
    if headline:
        print(headline.text)
        link = story.find('a')
        if link:
            print(link['href'])
        summary = story.find('p')
        if summary:
            print(summary.text)
