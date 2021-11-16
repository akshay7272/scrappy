from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

s = HTMLSession()

url = ('https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf')

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('a', {'class': 'ui-paginator-page ui-state-default ui-corner-all'})
    if not pages.find('a', {'class': 'ui-paginator-last ui-state-default ui-corner-all'}):
        url = 'https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf' + str(pages.find('a', {'class': 'ui-paginator-page ui-state-default ui-corner-all'}).find('a')['href'])
        return url
    else:
        return


while True:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url.text.strip())