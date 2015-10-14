# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
import pymysql.cursors
import time
import os
import sys
from threading import Thread

class Mysql(Thread):

	#Initial Connection
	def __init__(self, f_handler, start_num, total_page):
		Thread.__init__(self)
		self.connection = pymysql.connect(host = '127.0.0.1', user = 'admin', \
			password = '', db = 'test', charset = 'utf8mb4', \
			cursorclass = pymysql.cursors.DictCursor)
		self.cursor = self.connection.cursor()
		self.total_page = total_page
		self.gapTime = 2
		self.thread_stop = False
		self.f_handler = f_handler
		self.start_num = start_num

	#Get Current time
	def getCurrentTime(self):
		return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time())) + "\tMySQL:\t"

	#Insert data or update
	def insertData(self, word):
		try:
			sql = "INSERT INTO `statis` (`id`, `word`, `count`) VALUES (Null, %s, %s)"\
				+ " ON DUPLICATE KEY UPDATE `count` = `count` + 1"
			self.cursor.execute(sql, (word, 1))
			self.connection.commit()

		except Exception as e:
			self.connection.rollback()
			print (self.getCurrentTime(), "Exception:", e)

    #Read the stored file
	def readFile(self):
		fileDir = os.path.dirname(os.path.realpath('__file__'))
		for page_num in range(self.start_num, self.total_page + 1):
			filename = os.path.join(fileDir, 'dig/Snippets'+ str(page_num) + '.txt')
			print(self.getCurrentTime(), "Current file: Snippets", str(page_num))

			while not self.thread_stop and (not os.path.isfile(filename) or not os.access(filename, os.R_OK)):
				print(self.getCurrentTime(), "Fail to access the file, wait for",self.gapTime,"seconds")
				time.sleep(self.gapTime)

			if self.thread_stop:
				print(self.getCurrentTime(), "Stoped because of thread")
				return

			print (self.getCurrentTime(), "Start to read file:", filename)
			f = open(filename, 'r')
			count = 0

			for word in self.wordGenerator(f):
				self.insertData(word)
				count += 1

			print(self.getCurrentTime(), "Load", count, "words from file Snippets", str(page_num))
			print(self.getCurrentTime(), "Wait for",self.gapTime,"seconds to access the next file")
			time.sleep(self.gapTime)
			
		print(self.getCurrentTime(), "Load all files")

	#Return the word from file
	def wordGenerator(self, data):
		for line in data:
			for word in line.split():
				yield word.strip().lower()

	#Run
	def run(self):
		sys.stdout = self.f_handler
		print(self.getCurrentTime(), "Start to transfer data into MySQL")
		self.readFile()
		self.connection.close()
		print(self.getCurrentTime(), "Disconnect from MySQL")


	#stop
	def stop(self):
		self.thread_stop = True

