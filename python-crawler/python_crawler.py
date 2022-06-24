from email.charset import Charset
import requests
import time
from lxml import etree
from urllib.parse import urljoin

url = input()

def url_response(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'}
    time.sleep(5)
    try:
        response = requests.get(url,headers=headers)
    except :
        time.sleep(60)
        response = requests.get(url,headers=headers)
    response=response.text
    #response = response.encode('iso-8859-1')
    #response = response.decode('gbk').encode('utf8').decode('utf8')
    html=etree.HTML(response)
    return html

def url_a(html):
    xp = html.xpath('//a/@href')
    url = xp[22]
    return url

def url_url(a,url):
    return urljoin(url, a)

def url_title(html):
    title = html.xpath('//div/text()')
    title = title[16]
    return title

def url_essay(html):
    essay = html.xpath('//div[@id="content"]/p/text()')
    return essay

while True:
    xie_ru = open('text.txt','a')
    html = url_response(url)
    a = url_a(html)
    url = url_url(a,url)
    title = url_title(html)
    essay = url_essay(html)
    xie_ru.write((title + '\n'))
    print(title)
    print(essay)
    print(url)
    for aaa in range(len(essay)):
        essayx = essay[aaa]
        try:
            xie_ru.write(essayx+ '\n')
        except:
            pass
    del essay
    xie_ru.close()
