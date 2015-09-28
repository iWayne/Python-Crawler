import urllib
import urllib2
import re
import thread
import time
from bs4 import BeautifulSoup

#Class for QSBK
class QSBK:
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
		self.headers = {'User-Agent' : self.user_agent}
		self.stories = [] #For each paragraph
		self.enable = False #Whether Continue

	def getPage(self, pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			request = urllib2.Request(url, headers = self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8', 'ignore') #ignore malformed data and continue
			return pageCode

		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"Fail Reason"
				print e.reason
				return None

	def getPageItems(self, pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print "Fail to load webpage..."
			return None
		pattern = re.compile('<div.*?author">.*?' + 
			'<img.*?>(.*?)</a>.*?' + 
			'<div.*?content">(.*?)<!--(.*?)-->.*?' + 
			'</div>(.*?)' +
			'<div.*?stats".*?number">(.*?)</i>', re.S)
		items = re.findall(pattern, pageCode)
		pageStories = []
		for item in items:
			haveImg = re.search("img", item[3])
			if not haveImg:
				replaceBR = re.compile('<br/>')
				text = re.sub(replaceBR, "\n", item[1])
				pageStories.append([item[0].strip(), text.strip(), item[2].strip(), item[4].strip()])
		return pageStories

	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1

	def getOneStory(self,pageStories,page):
		for story in pageStories:
			input = raw_input()
			self.loadPage()
			if input == "q":
				self.enable = False
				return
			print u"No.%dPage\tPoster:%s\tID:%s\tLike:%s\n%s" %(page,story[0], story[2], story[3], story[1])

	def start(self):
		print u"Reading, press q to quit"
		self.enable = True
		self.loadPage()
		if len(self.stories) > 0:
			print u"Ready!"
		nowPage = 0
		while self.enable:
			if len(self.stories) > 0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories,nowPage)
crawl = QSBK()
crawl.start()
