import csv
import requests 
from bs4 import BeautifulSoup
for i in range(907):      # Number of pages plus one 
    url = "https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf".format(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    print(soup.text.strip())