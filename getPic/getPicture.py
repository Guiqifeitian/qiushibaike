#-*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys
import re
import time

#等待多线程优化
def getHtml(page = 5):
    for i in range(1,page+1):
        url = 'http://www.qiushibaike.com/pic/page/'+str(i)+'/?s=4959209'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        req = urllib2.Request(url, headers = header)
        res = urllib2.urlopen(req)
        content = res.read().decode('utf-8')
        analyzeHtml(content,i)

def analyzeHtml(content,i):
    soup = BeautifulSoup(content,'lxml')
    content = soup.find_all('img')

    name = 0
    for each in content:
        pic_url = each.get('src')
        pic_name = each.get('alt')
        if re.match('http',pic_url):
            time.sleep(1)
            name += 1
            try:
                pic = urllib2.urlopen(pic_url)
                with open(sys.path[0]+u'/pic/第'+str(i)+u'页第'+str(name)+u'张.png','wb') as f:
                    f.write(pic.read())
            except Exception,e:
                print str(e)


def test():
    # sys.path[0]+'/pic/'
    pic_url = 'http://pic.qiushibaike.com/system/pictures/11860/118604728/medium/app118604728.jpg'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    req = urllib2.Request(pic_url, headers=header)
    file = urllib2.urlopen(req)
    with open(sys.path[0]+'/pic/cc.png','wb') as f:
        f.write(file.read())



def main():
    page = input('enter the number of pages:')
    t1 = time.time()
    getHtml(page)
    t2 = time.time()
    print 'time cost:' + str(t2 - t1) + 's'

if __name__ == '__main__':
    main()