# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
'''
Created by Wei Shan

Fill the linkedin UserID and Password before running
'''

import requests
from bs4 import BeautifulSoup
import re
import os
import time
import sys
import tool

class Spider(object):

	#Initialize
	def __init__(self):
		self.page_num = 1
		self.total_num = 2
		self.client = None
		self.userID = 'User'
		self.pwd = 'pwd'

	#Login Linkedin and store Session info
	def loginLinkedin(self):
		client = requests.Session()
		HOMEPAGE_URL = 'https://www.linkedin.com'
		LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
		html = client.get(HOMEPAGE_URL).content
		soup = BeautifulSoup(html, "lxml")
		csrf = soup.find(id="loginCsrfParam-login")['value']
		login_information = {
		'session_key':self.userID,
		'session_password':self.pwd,
		'loginCsrfParam': soup.find(id="loginCsrfParam-login")['value'],
		}
		post = client.post(LOGIN_URL, data=login_information)
		return client

	#Get current time
	def getCurrentTime(self):
		return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

	#Create the target LOGIN_URL
	def getPageURLByNum(self, page_num):
		page_url = "https://www.linkedin.com/vsearch/p?rsid=4004260481443401945874&keywords=seeking%20job&trk=vsrp_people_cluster_header&trkInfo=VSRPsearchId%3A4004260481443401940205,VSRPcmpt%3Apeople_cluster&openFacets=N,G,CC&page_num="\
		+ str(page_num) + "&pt=people"
		return page_url

	#Refine information and store into files
	def storeAndRefinedContent(self, items, page_num):
		fileDir = os.path.dirname(os.path.realpath('__file__'))
		filename = os.path.join(fileDir, 'dig/Snippets'+ str(page_num) + '.txt')
		print (self.getCurrentTime(), "OpenFile:", filename)
		file = open(filename, 'w')
		filt = tool.Tool()
		for item in items:
			item = filt.replace(item)
			if len(item) > 0:
				file.write(item + '\n\n')
		file.close()
		print (self.getCurrentTime(), "Finish Storage")


	#Store the source code from response
	def storeSourceCode(self, text, page_num):
		fileDir = os.path.dirname(os.path.realpath('__file__'))
		filename = os.path.join(fileDir, 'source/SourceCode'+ str(page_num) + '.txt')
		f = open(filename,'w')
		f.write(text)
		f.close
		print(self.getCurrentTime(), "Store the source code at", filename)

	#Crawl each pages
	def getPages(self, page_num, client):
		#Need to catch exception here
		try:
			content = client.get(self.getPageURLByNum(page_num), timeout = 5)
		except requests.exceptions.RequestException as e:
			print(self.getCurrentTime(), "Timeout when get page#", page_num, e)

		print (self.getCurrentTime(), "Reponse Code: ", content.status_code)
		text = content.text
		self.storeSourceCode(text, page_num)
		pattern = re.compile('snippets":\[\{(.*?)\}\]', re.S)
		items = re.findall(pattern, text)
		print (self.getCurrentTime(), "Find", len(items), "Snippets")

		self.storeAndRefinedContent(items, page_num)
		print (self.getCurrentTime(), "Finish page #", str(page_num))

		#Check if use is forced loging out
		if len(items) == 0:
			if self.isLogedOut(text):
				print(self.getCurrentTime(), "User has been logged out")
				time.sleep(3)
				self.client = self.loginLinkedin()
				print(self.getCurrentTime(), "Login again")
				return False
		return True


	#Check user status
	def isLogedOut(self, text):
		keyLogout = re.compile('login_reg_redirect')
		items = re.findall(keyLogout, text)
		return len(items) > 0


	#Main
	def main(self):
		f_handler = open('spider.log', 'w')
		sys.stdout = f_handler
		print(self.getCurrentTime(), "Start to login Linkedin")
		self.client = self.loginLinkedin()
		print(self.getCurrentTime(), "Get the session")
		print (self.getCurrentTime(), "Crawler is running")

		self.page_num = 1
		while self.page_num <= self.total_num:
			print (self.getCurrentTime(), "Crawling page:", self.page_num)
			try:
				statusCorrect = self.getPages(self.page_num, self.client)
				if statusCorrect:
					self.page_num += 1
				else:
					print(self.getCurrentTime(), "Some problem with page#", self.page_num, ". Try again later")
				time.sleep(10)
			except Exception as e:
				print (self.getCurrentTime(), "Exception:", e)
		print(self.getCurrentTime(), "Finish all pages")

spider = Spider()
spider.main()
