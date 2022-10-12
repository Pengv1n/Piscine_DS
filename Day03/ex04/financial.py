#!/bin/python3

import sys
import time
from bs4 import BeautifulSoup
import requests

def financial(ticker, field):
    url = 'https://finance.yahoo.com/quote/' + ticker + '/financials'
    page = requests.get(url, headers={'User-Agent': 'Custom'})
    page_parsed = BeautifulSoup(page.text, 'html.parser')
    title = page_parsed.title.string
    if title == 'Symbol Lookup from Yahoo Finance':
        raise Exception('Wrong ticker')
    tags = page_parsed.find_all(attrs={'data-test': 'fin-row'})
    rows = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if field not in rows:
        raise Exception('Error with field')
    elems = tags[rows.index(field)].find_all('span')
    return tuple(elem.get_text() for elem in elems)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(financial(sys.argv[1], sys.argv[2]))
