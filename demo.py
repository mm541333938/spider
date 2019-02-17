# coding:utf-8
# 实现一个简单的爬虫，爬取图片
import urllib
import urllib.request
import re


# 根据url 获取网页html内容
def getHtmlContent(url):
    page = urllib.request.urlopen(url)
    return page.read().decode('utf-8')

# 从html中解析出jpg图片的url
def getJPGs(html):
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')
    # 解析出jpg 的url列表
    jpgs = re.findall(jpgReg, html)
    return jpgs

def downloadJPG(imgUrl, fileName):
    urllib.request.urlretrieve(imgUrl, fileName)

def batchDownloadJPGs(imgUrls, path = 'D:\\picture\\'):
    count = 1
    for url in imgUrls:
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        count += 1

def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)