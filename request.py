import requests
import re
import json
import time
#import os,pymysql
headers ={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Referer': 'http://www.mzitu.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36'
}
regex = '<img src="([\w\W]*?)"'
def getImage(imagesUrl,span,filesname):
    time.sleep(0.5)
    for n in range(1, span+1):
        imageurl = imagesUrl+"/"
        if n == 1:
            currentSpan = ""
        else:
            currentSpan = str(n)
        imageurl = imageurl + currentSpan
        # time.sleep(0.2)
        urlText = requests.get(imageurl, headers=headers).text
        imageHtml = re.findall(regex, urlText)
        imageHtml = str(imageHtml[0])
        image = requests.get(imageHtml, headers=headers)
        image = image.content
        if not os.path.exists("f:\\mzitu\\" + filesname):
            os.mkdir("f:\\mzitu\\" + filesname)

        with open("f:\\mzitu\\" + filesname + "\\" + str(currentSpan) + ".jpg", "wb") as f:
            f.write(image)
            f.close()
def getUrlList():
    url ="http://www.xxxx.com/"
    regex = '<li><a href="([\w\W]*?)"'
    html = requests.get(url)
    urlList = re.findall(regex,html.text)
    print(urlList)
    return urlList
def download(url):
    #获取页面信息
    html = requests.get(url)
    # print (html.text)
    regex = "…</span><a href='"+url+"/"+"([\w\W]*?)'>"
    print(regex)
    #解析最大页数
    span = re.findall(regex,html.text)
    span = int(span[0])
    #print(span)
    #getImage(html.text,span,url[-6:])
    #getImage(html.text,span,url[-6:])
    return url,span,url[-6:]
def main():
    urlList=getUrlList()
    for url in urlList:
        imagesUrl,span,filesName = download(url)
        getImage(imagesUrl,span,filesName)

main()
