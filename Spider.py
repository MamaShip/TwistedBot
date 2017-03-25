# -*- coding: utf-8 -*-
import urllib, urllib2
import re
import os
import itertools
from string import maketrans

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
values = {'username': '', 'password': ''}
headers = {'User-Agent': user_agent}
postdata = urllib.urlencode(values)

savePath = '/root/bot/'

str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}
table = maketrans('wkv1ju2it3hs4g5rq6fp7eo8dn9cm0bla','abcdefghijklmnopqrstuvw1234567890')


#图片URL解码
def decode(url):
    for key, value in str_table.items():
        url = url.replace(key, value)
    url = url.translate(table)
    return url


#构造搜索用的URL，返回搜索用URL序列（type是generator，因为用了itertools.count）
def buildUrl(keyword='猫 萌萌'):
    word = urllib.quote(keyword)
    url = r"https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&face=0&istype=2&qc=&nc=1&fr=&pn={pn}&rn=30"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=30))
    return urls


#获得一个URL的html，返回字符串
def getHtml(url):
    req = urllib2.Request(url=url, headers=headers)
    page = urllib2.urlopen(req)
    html = page.read()
    return html


#在html中搜索图片URL，返回图片URL列表
def getImage(html):
    reg = r'"objURL":"(ippr_.*?)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    imgUrls = [decode(x) for x in imglist]
    return imgUrls


#从图片URL列表中，保存可访问的图片URL，按行保存在imageUrls.txt中
def saveUrl(urls, path=savePath):
    if not os.path.isdir(path):
        os.mkdir(path)
    file = open('%simageUrls.txt' % savePath, mode='a')
    for imageUrl in urls:
        print "Saving: %s" % imageUrl
        try:
            req = urllib2.Request(imageUrl)
            response = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            continue
        except urllib2.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
            continue
        file.write('%s\n' % imageUrl)
        file.flush()
        num[0] += 1
        if num[0] == setNum[0]:
            break
    file.close()


if __name__ == '__main__':
    keyword = raw_input("请输入要下载的图片关键词：(直接回车默认为“猫 萌萌”)\n") or '猫 萌萌'
    setNum = [int(raw_input("请输入需要图片数量：(直接回车默认无限)\n") or -1)]
    urls = buildUrl(keyword)
    num = [0]
    for url in urls:
        html = getHtml(url)
        imageList = getImage(html)
        if len(imageList) == 0:
            break
        saveUrl(imageList)
        if num[0] == setNum[0]:
            break
    print "共保存%s张图片" % num[0]
