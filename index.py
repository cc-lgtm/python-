# https://www.duitang.com/search/?kw=%E5%B0%8F%E5%A7%90%E5%A7%90&type=feed
# https://www.duitang.com/napi/blog/list/by_search/?kw=%E5%B0%8F%E5%A7%90%E5%A7%90&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start=24&_=1609650766881

import requests
import json
import jsonpath
import urllib.parse

url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'
kw = '小姐姐'
keyword = urllib.parse.quote(kw)
num = 1
for index in range(0, 73, 24):
    url = url.format(keyword, index)
    res = requests.get(url)
    resp = res.text
    html = json.loads(resp)
    photos = jsonpath.jsonpath(html, '$..path')
    for i in photos:
        a = requests.get(i)
        with open(r'/home/coderking/学习/python爬美女图片/photos/{}.jpg'.format(num), 'wb') as fp:
            fp.write(a.content)
            num += 1