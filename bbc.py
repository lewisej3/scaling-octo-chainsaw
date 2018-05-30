#!/usr/local/bin/python3

import datetime
import sqlite3
import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.bbc.co.uk/news')
soup = BeautifulSoup(response.text, 'html.parser')

now = datetime.datetime.now()
currentdatetime = now.strftime("%Y-%m-%d %H:%M")
sqlite_file = 'bbcnews.sqlite'    # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def add_item_sum(category):
    c.execute('''INSERT INTO News(Headlines, Summary, Link, Date, Type) \
        VALUES (?, ?, ?, ?, ?)''', [headline.text, summary.text, link['href'], currentdatetime, category])
    return 0
def add_item_nosum(category):
    c.execute('''INSERT INTO News(Headlines, Summary, Link, Date, Type) \
        VALUES (?, ?, ?, ?, ?)''', [headline.text, " ", link['href'], currentdatetime, category])
    return 0

# Creating a new SQLite table
try:
    c.execute('''CREATE TABLE News
              (Headlines TEXT,
               Summary TEXT,
               Link TEXT,
               Date TEXT,
        Type TEXT)''');
except:
    pass

# Find the primary headline and input as new row in table.

primary = soup.find('div',{'class': 'nw-c-top-stories-primary__story'} )
headline =primary.find('h3')
summary = primary.find('p')
link = primary.find('a')
add_item_sum("Primary")

# Find the secondary headlines and input as new rows in tables.
# If the secondary headline doesn't have a summary then it adds a blank space
secondaries = soup.find_all('div',{'class': 'nw-c-top-stories__secondary-item'} )
for secondary in secondaries:
    headline = secondary.find('h3')
    summary = secondary.find('p')
    link = secondary.find('a')
    if summary:
        add_item_sum("Secondary")
    else:
        add_item_nosum("Secondary")

# Find the tertiary headlines and input as new rows in tables
tertiary = soup.find('div',{'class': 'nw-c-top-stories__tertiary-items'})
stories = tertiary.find_all('div',{'class': 'gel-layout__item'})
for story in stories:
    headline = story.find('h3')
    link = story.find('a')
    add_item_nosum("Tertiary")

# Find the Sport's headlines with links

sport = soup.find('div',{'class': 'nw-c-sport'})
stories = sport.find_all('div', { 'class': 'gs-c-promo' })
for story in stories:
    headline = story.find('h3')
    link = story.find('a')
    add_item_nosum("Sport")


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
