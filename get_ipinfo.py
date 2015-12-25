#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib,urllib2
import re
 
def checkip(ip):
    URL = 'http://www.ip138.com/ips138.asp'
    _params={'action':2,'ip':ip}
    data = urllib.urlencode(_params)
    req = urllib2.Request(URL,data)
    response= urllib2.urlopen(req)
    f=str(response.read().decode('gb2312').encode('utf8'))
    regex=re.compile(r'class=\"ul1\"\>\<li\>本站主数据：(.*)\<\/li\>\<li\>')
    pipei=regex.findall(f)
    for i in pipei:
        print str(i)

if __name__ == '__main__':
    checkip()
