import time
import mysql
import spider
import threading

def test():
	f_handler = open('spider2.log', 'w')

	try:
		start_page_num = 1
		total_page_num = 100
		mysqlThrd = mysql.Mysql(f_handler, start_page_num, total_page_num)
		#spiderThrd = spider.Spider(f_handler, start_page_num, total_page_num)
		#spiderThrd.start()
		#time.sleep(2)
		mysqlThrd.start()
	except:
		#spiderThrd.stop()
		mysqlThrd.stop()
		print("Stop Missions by Exception")
	

	inputLine = input()
	if inputLine == "Q":
		#spiderThrd.stop()
		mysqlThrd.stop()
		print ("Stop Missions by Admin")

if __name__ == '__main__':
	test()