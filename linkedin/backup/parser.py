# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import os
import time

class Filter:
	removeScript = re.compile(r'\\u003.*?\\u003e')
	removeNextLine = re.compile(r'\\n')
	removeFmtHeading = re.compile(',"fmt_heading":".*?"')
	removeFmtBody = re.compile(',"fmt_body":".*?"')
	removeBlock = re.compile('\},{')
	removeBlock2 = re.compile('\[')
	removeBlock3 = re.compile('\]')
	removeUnicode = re.compile(r'\\u....')
	findContent = re.compile('"fieldName":"(.*?)",.*?:.*?"(.*?)eeking(.*?)"')
	removePunc = re.compile('\W')

	def replace(self, x):
		x = re.sub(self.removeScript,"",x)
		x = re.sub(self.removeNextLine," ",x)
		x = re.sub(self.removeBlock,"\n",x)
		x = re.sub(self.removeBlock2,"",x)
		x = re.sub(self.removeBlock3,"",x)
		x = re.sub(self.removeFmtHeading, "",x)
		x = re.sub(self.removeFmtBody, "",x)
		x = re.sub(self.removeUnicode, " ", x)
		items = re.findall(self.findContent, x)
		str = ""
		for item in items:
			if item[0] == 'Current':
				str = item[1] + 'eeking' + item[2]
			if item[0] == 'Summary':
				str = item[1] + 'eeking' + item[2]
		str = re.sub(self.removePunc," ", str)
		return str.strip().lower()


f = open('test1.html')
data = f.read()
f.close()
pattern = re.compile('snippets":\[\{(.*?)\}\]', re.S)
items = re.findall(pattern, data)
print (len(items))
##print (data)
fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'source/WriteSnippets'+ str(1) + '.txt')
file = open(filename, 'w')
filter = Filter()
for item in items:
	item = filter.replace(item)
	if len(item) > 0:
		file.write(item + '\n' + '\n')
file.close()




