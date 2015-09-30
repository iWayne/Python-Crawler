# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

f = open('test.html')
data = f.read()
f.close()
pattern = re.compile('snippets":[(.*?)]', re.S)
items = re.findall(pattern, data)
print (len(items))
##print (data)
for item in items:
	print (item + '\n')
