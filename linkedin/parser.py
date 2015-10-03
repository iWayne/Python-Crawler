# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

class Filter:
	removeScript = re.compile(r'\\u003.*?\\u003e')
	removeNextLine = re.compile(r'\\n')
	removeFmtHeading = re.compile(',"fmt_heading":".*?"')
	removeFmtBody = re.compile(',"fmt_body":".*?"')
	removeBlock = re.compile('\},{')
	removeBlock2 = re.compile('\[')
	removeBlock3 = re.compile('\]')
	findContent = re.compile('"fieldName":"(.*?)",.*?:.*?"(.*?)eeking(.*?)"')

	def replace(self, x):
		x = re.sub(self.removeScript,"",x)
		x = re.sub(self.removeNextLine," ",x)
		x = re.sub(self.removeBlock,"\n",x)
		x = re.sub(self.removeBlock2,"",x)
		x = re.sub(self.removeBlock3,"",x)
		x = re.sub(self.removeFmtHeading, "",x)
		x = re.sub(self.removeFmtBody, "",x)
		items = re.findall(self.findContent, x)
		str = ""
		for item in items:
			if item[0] == 'Current':
				str = item[1] + 'eeking' + item[2]
			if item[0] == 'Summary':
				str = item[1] + 'eeking' + item[2]
		return str


f = open('test.html')
data = f.read()
f.close()
pattern = re.compile('snippets":\[\{(.*?)\}\]', re.S)
items = re.findall(pattern, data)
print (len(items))
##print (data)
file = open('WriteSnippets1.txt', 'w')
filter = Filter()
for item in items:
	item = filter.replace(item)
	if len(item) > 0:
		file.write(item + '\n' + '\n')
file.close()




