import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
with open('aa.html','r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for i in range(900):
        

     for tag in soup.find_all('tr'):
       
       print(f'{tag.text}')
   
     


