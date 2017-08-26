from urllib.parse import urlencode
from config import *
import requests
from requests.exceptions import  ConnectionError
from pyquery import PyQuery as pq
import pymongo

#代理信息
proxy = None

#mongod的信息
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

#获取代理
def get_proxy():
    try:
        response = requests.get(PROXY_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None
#获取html
def get_html(url, count = 1):
    print('get_html', url)
    print('count:', count)
    global proxy
    if count > MAX_COUNT:
        print("try to many times")
        return None
    print('proxy', proxy)
    try:
        if proxy:
            proxies = {
                'http':'http://' + proxy
            }
            response = requests.get(url, allow_redirects = False, headers = headers, proxies = proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        print('response_code', response.status_code)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print('chunkError', response.status_code)
            proxy = get_proxy()
            if proxy:
                count += 1
                return get_html(url, count)
            else:
                print('proxy is fail')
                return None
    except ConnectionError as e:
        print('Eror:', e.args)
        count += 1
        proxy = get_proxy()
        return get_html(url, count)
#获取列表页信息
def get_index(keyword, page):
    data = {
        'query':keyword,
        'type':2,
        'page':page
    }
    queries = urlencode(data)
    url = BASE_URL + queries
    html = get_html(url)
    return html

#解析index页
def parse_index(content):
    doc = pq(content)
    items = doc.find('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

#解析详细信息
def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code ==200:
            return response.text
        return None
    except ConnectionError:
        return None

#解析详细信息
def parse_detail(content):
    doc = pq(content)
    title = doc('#activity-name').text()
    content = doc('#meta_content').text()
    date = doc('#post-date').text()
    nickname = doc('#post-user').text()
    author = doc('#meta_content > em:nth-child(3)').text()
    return {
        'title':title,
        'content':content,
        'date':date,
        'nickname':nickname,
        'author':author
    }

def main():
    for page in range(1, 101):
        html = get_index(KEY_WORD, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_content = parse_detail(article_html)
                    save_to_db(article_content)

#保存信息到mongodb
def save_to_db(data):
    if db[MONGO_TABLE].update({'title':data['title']}, {'$set': data}, True):
        print('保存数据成功', data['title'])
    else:
        print("保存数据失败", data['title'])

if __name__ == '__main__':
    main()
