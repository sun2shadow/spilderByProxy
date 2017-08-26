#请求头信息
BASE_URL = 'http://weixin.sogou.com/weixin?'
headers = {
    'Cookie':'SUV=1503642112000711; SMYUV=1503642112001508; UM_distinctid=15e180dd23019d-0a186d63bebef8-24414032-fa000-15e180dd2314c; IPLOC=CN3100; SUID=DF82ABB41808990A00000000599FC201; ABTEST=3|1503642117|v1; SNUID=3F624B6BE0E5885216A56C48E0EDEC7C; weixinIndexVisited=1; JSESSIONID=aaalrBO0fbHqw4aJAVi4v; LSTMV=364%2C32; LCLKINT=1901; PHPSESSID=n22r9mafen98s0d8bi6vuo4ag6; SUIR=3F624B6BE0E5885216A56C48E0EDEC7C; sct=10; ppinf=5|1503645490|1504855090|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OlN1bm55fGNydDoxMDoxNTAzNjQ1NDkwfHJlZm5pY2s6NTpTdW5ueXx1c2VyaWQ6NDQ6bzl0Mmx1SHVnQ2h2dXR5UVVqeWFLd2Vfb2hRVUB3ZWl4aW4uc29odS5jb218; pprdig=FrV_V3ImaRCRWswYgnq9HS_kVnYgT3QGukdNr8nbBomC7ws4uyW_OVDQyRNPw54UCqY9cu8y4_pPsldYnja5r4EjpuRmBAyE1QrvTTfokvbmYdLehL6idggmSckKv3qCM51Y0ue039i9mtNMP1_Ec6OIa4l75yF87gmBh4m9G7E; sgid=31-30498125-AVmfzzJZBicSjRNuamaeWvZI; ppmdig=150364549100000045e887cdf1772ed1cf8a47eedc74007b',
    'Host':'weixin.sogou.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36'
}
#代理信息
PROXY_URL = 'http://localhost:5000/get'

#mongodb
MONGO_URL = 'localhost'
MONGO_DB = 'weixin'
MONGO_TABLE = 'articles'

KEY_WORD = '风景'
MAX_COUNT = 5