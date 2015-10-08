# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
import pymysql.cursors

user = 'admin'
pwd = ''
host = '127.0.0.1'
db = 'test'

connection = pymysql.connect(host = host, user = user, \
	password = pwd, db = db, charset = 'utf8mb4', \
	cursorclass = pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:
		sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
		cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
		sql = "INSERT INTO `statis` (`id`, `word`, `count`) VALUES (Null, %s, %d)"\
			+ " ON DUPLICATE KEY UPDATE `count` = `count` + 1"
		cursor.execute(sql, ('', 1))
	connection.commit()
	'''
	with connection.cursor() as cursor:
		sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
		cursor.execute(sql, ('webmaster@python.org',))
		result = cursor.fetchone()
		print(result)
	'''

finally:
	connection.close()



#INSERT INTO statis (id, word, count) VALUES(NULL, "A", 20) ON DUPLICATE KEY UPDATE count=count + 1;