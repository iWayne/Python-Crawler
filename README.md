_Last Updated: Mon., Oct. 12th, 2015  @ 11:30A_

### Python-Crawler

Welcome!

This repository contains some crawlers' source code for crawling jokes from [qiushibaike.com](www.qiushibaike.com) and search reuslt for LinkedIn search page.

____

###REQUIREMENT

Python 3.5 with BeautifulSoup4, Requests, Pymysql

Mysql version above 5.2

____

###Documents

#### QSBK floder:

The python program used to crawl the jokes from [qiushibaike.com](www.qiushibaike.com). Fetch next joke by pressing Enter button. and quit by entering 'Q'.


####Linkedin

The python program that can crawl information from LinkedIn Search page. LinkedIn search API is no longer available, so I implement the Requests for requesting content, use BeautifulSoup4 and Regex to figure out the info, and use pymysql to insert data into MySQL databse.

Resouces floder is used to store the source code of webpage fo debuging.

Dig floder stores the refined information.

Spider and mysql are separately programs extending threads. And enter 'Q' to stop thread.


____

###REFERENCE

 -[Tutor](http://cuiqingcai.com/1052.html)
 
 -[Pymysql](https://github.com/PyMySQL/PyMySQL)
