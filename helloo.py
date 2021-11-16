import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
page = ""
url = 'https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf'+str(page)
#Use the browser to get the URL. This is a suspicious command that might blow up.
page= requests.get(url)

print(page.headers.get("content-type", "unknown"))
print(page.text.strip())