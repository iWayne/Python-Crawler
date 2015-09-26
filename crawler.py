# -*- coding:utf-8 -*-
import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent' : user_agent}
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	print response.read()
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason