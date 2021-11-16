#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from urllib import parse



URL = 'https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf'

s = requests.Session()

r = s.get(URL)

JSESSIONID = s.cookies['JSESSIONID']

soup = BeautifulSoup(r.content, "html.parser")

javax_faces_ViewState = soup.find_all("div",class_= 'ui-datatable-tablewrapper')


d = {}

d['javax.faces.partial.ajax']= "true"
d['javax.faces.source: ocrForm']="reportResultTable"
d['javax.faces.partial.execute']= "ocrForm:reportResultTable"
d['javax.faces.partial.render']= "ocrForm:reportResultTable"
d['javax.faces.behavior.event']= "page"
d['javax.faces.partial.event']= "page"
d['ocrForm:reportResultTable_pagination']= "true"
d['ocrForm:reportResultTable_first']= 1000
d['ocrForm:reportResultTable_rows']= 1000
d['ocrForm:reportResultTable_skipChildren']= "true"
d['ocrForm:reportResultTable_encodeFeature']= "true"
d['ocrForm']= "ocrForm"
d['ocrForm:reportResultTable_rppDD']= 1000
d['javax.faces.ViewState']= javax_faces_ViewState





h = {}
h['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
h['Accept-Encoding'] = 'gzip, deflate'
h['Accept-Language'] = 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
h['Cache-Control'] = 'max-age=0'
h['Connection'] = 'keep-alive'
h['Content-Length'] = '10000'
h['Content-Type'] = 'application/x-www-form-urlencoded'
h['Cookie'] = '_ga=91A022E04C90B77136785A5CA7B6D452; JSESSIONID={}; _gid=91A022E04C90B77136785A5CA7B6D452'.format(JSESSIONID)
h['Host'] = 'www.ocrportal.hhs.gov'
h['Origin'] = 'https://ocrportal.hhs.gov'
h['Referer'] = 'https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf'
h['Upgrade-Insecure-Requests'] = '1'
h['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
h['X-Requested-With'] = "XMLHttpRequest"










URL2 = 'https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf;JSESSIONID=' + str(JSESSIONID)
post_response = s.post(URL2, headers=h, data=d)


soup = BeautifulSoup(post_response.text, "html.parser")
javax_faces_ViewState = soup.find_all("tbody")


def f_headers(JSESSIONID):
    headers = {}
    headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    headers['Accept-Encoding'] = 'gzip, deflate'
    headers['Accept-Language'] = 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
    headers['Connection'] = 'keep-alive'
    headers['Content-Length'] = '20000'
    headers['Content-type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
    headers['Cookie'] = '_ga=91A022E04C90B77136785A5CA7B6D452; JSESSIONID=' + str(JSESSIONID)
    headers['Faces-Request'] = 'partial/ajax'
    headers['Host'] = 'www.ocrportal.hhs.gov'
    headers['Origin'] = 'https://ocrportal.hhs.gov'
    headers['Referer'] = 'https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf'
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    headers['X-Requested-With'] = "XMLHttpRequest"
    
    

    return headers

    



def build_data(data, n, javax_faces_ViewState):

    if n == 1:
        data['javax.faces.partial.ajax']= "true"
        data['javax.faces.source: ocrForm']="reportResultTable"
        data['javax.faces.partial.execute']= "ocrForm:reportResultTable"
        data['javax.faces.partial.render']= "ocrForm:reportResultTable"
        data['javax.faces.behavior.event']= "page"
        data['javax.faces.partial.event']= "page"
        data['ocrForm:reportResultTable_pagination']= "true"
        data['ocrForm:reportResultTable_first']= 0
        data['ocrForm:reportResultTable_rows']= 20
        data['ocrForm:reportResultTable_skipChildren']= "true"
        data['ocrForm:reportResultTable_encodeFeature']= "true"
        data['ocrForm']= "ocrForm"
        data['ocrForm:reportResultTable_rppDD']= 100
        data['javax.faces.ViewState']= javax_faces_ViewState


data = {}
build_data(data, 1, javax_faces_ViewState)

headers = f_headers(JSESSIONID)

post_response = s.post(URL, headers=headers, data=data)

print(post_response.text.strip())


with open("archive.txt", "w") as file:
    file.write(post_response.text.strip())
