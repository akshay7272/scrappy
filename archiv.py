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
# d['ocrForm']="j_idt24:"
d['ocrForm:reportResultTable_rppDD']= 100
d['javax.faces.ViewState']= javax_faces_ViewState





h = {}
h['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
h['Accept-Encoding'] = 'gzip, deflate, br'
h['Accept-Language'] = 'en-GB,en-US;q=0.9,en;q=0.8'
h['Connection'] = 'keep-alive'
h['Content-Length'] = '156855'
h['Content-type'] = 'text/html;charset=UTF-8'
h['Cookie'] = "_ga=E7523F1DCEDAEF44C4F0A7C347B03C86;JSESSIONID=" + str(JSESSIONID)
h['Faces-Request'] = 'partial/ajax'
h['Host'] = 'www.ocrportal.hhs.gov'
h['Origin'] = 'https://ocrportal.hhs.gov'
h['Referer'] = 'https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf'
h['sec-ch-ua']="Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"
h['sec-ch-ua-mobile']='?0'
h['Upgrade-Insecure-Requests']='1'
h['sec-ch-ua-platform']= "Linux"
h['Sec-Fetch-Dest']= 'empty'
h['Sec-Fetch-Mode']='cors'
h['Sec-Fetch-Site']='sam-'
h['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
h['X-Requested-With'] = "XMLHttpRequest"
h['Strict-Transport-Security']= 'max-age=31557600; includeSubDomains'










URL2 = 'https://ocrportal.hhs.gov/ocr/breach/breach_report'
post_response = s.post(URL2, headers=h, data=d)


soup = BeautifulSoup(post_response.text, "html.parser")
javax_faces_ViewState = soup.find_all("div",class_= 'ui-datatable-tablewrapper')


def f_headers(JSESSIONID):
    headers = {}
    headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    headers['Accept-Encoding'] = 'gzip, deflate, br'
    headers['Accept-Language'] = 'en-GB,en-US;q=0.9,en;q=0.8'
    headers['Connection'] = 'keep-alive'
    headers['Content-Length'] = '156855'
    headers['Content-type'] = 'text/html;charset=UTF-8'
    headers['Cookie'] = "_ga=E7523F1DCEDAEF44C4F0A7C347B03C86;  JSESSIONID=" + str(JSESSIONID)
    headers['Faces-Request'] = 'partial/ajax'
    headers['sec-ch-ua']="Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"
    headers['sec-ch-ua-mobile']='?0'
    headers['sec-ch-ua-platform']= "Linux"
    headers['Sec-Fetch-Dest']= 'document'
    headers['Sec-Fetch-Mode']='navigate'
    headers['Sec-Fetch-Site']='same-origin'
    headers['Upgrade-Insecure-Requests']='1'
    headers['Host'] = 'www.ocrportal.hhs.gov'
    headers['Origin'] = 'https://ocrportal.hhs.gov'
    headers['Referer'] = 'https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf'
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    headers['X-Requested-With'] = "XMLHttpRequest"
    headers['Strict-Transport-Security']= 'max-age=31557600; includeSubDomains'
    





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
        data['ocrForm:reportResultTable_rows']= 2
        data['ocrForm']= "ocrForm"

        data['ocrForm']="j_idt24"
        data['ocrForm:reportResultTable_rppDD']= 100
        data['javax.faces.ViewState']= javax_faces_ViewState



data = {}
build_data(data, 1, javax_faces_ViewState)

headers = f_headers(JSESSIONID)

post_response = s.post(URL, headers=headers, data=data)

print(post_response.text.strip())


