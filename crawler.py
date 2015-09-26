import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent' : user_agent}
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
		'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
	content = response.read().decode('utf-8', 'ignore') #ignore malformed data and continue
	items = re.findall(pattern,content)
	for item in items:
		haveImg = re.search("img",item[3])
		if not haveImg:
			print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason