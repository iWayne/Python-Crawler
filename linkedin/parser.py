# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

class Tool:
	removeLeft = re.compile()



f = open('test.html')
data = f.read()
f.close()
pattern = re.compile('snippets":\[\{(.*?)\}\]', re.S)
items = re.findall(pattern, data)
print (len(items))
##print (data)
file = open('WriteSnippets.txt', 'w')
for item in items:
	file.write(item + '\n' + '\n')
file.close()




