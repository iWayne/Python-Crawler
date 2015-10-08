import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'source/Snippets'+ str(1) + '.txt')
f = open(filename, 'r')
for line in f:
	for word in line.split():
		print(word.strip(), '\n')
