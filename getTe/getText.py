#-*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

def getHtml(page = 5):
    for i in range(1,page+1):
        url = 'http://www.qiushibaike.com/text/page/'+str(i)+'/?s=4959167'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        req = urllib2.Request(url, headers = header)
        res = urllib2.urlopen(req)
        content = res.read().decode('utf-8')
        analyzeHtml(content)

def analyzeHtml(content):
    soup = BeautifulSoup(content,'lxml')
    content = soup.find_all('div',class_ = 'content')
    #print len(content)
    with open('qiushitext.txt','a') as f:
        for each in content:
            #print each.contents[1].text #前后各带一个换行符，中间、也即第1个是子标签
            f.write('  ')
            f.write(each.contents[1].text.encode('utf-8'))
            f.write('\n')

def main():
    page = input('enter the number of pages:')
    getHtml(page)

if __name__ == '__main__':
    main()