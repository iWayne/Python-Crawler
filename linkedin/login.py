# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "lxml")
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key':'email',
    'session_password':'pws',
    'loginCsrfParam': csrf,
}

post = client.post(LOGIN_URL, data=login_information)

content = client.get('https://www.linkedin.com/vsearch/p?rsid=4004260481443401945874&keywords=seeking%20job&trk=vsrp_people_cluster_header&trkInfo=VSRPsearchId%3A4004260481443401940205,VSRPcmpt%3Apeople_cluster&openFacets=N,G,CC&page_num=1&pt=people')

print (content.status_code)
print (content.encoding)

fh = open('defaultED.html','w')
fh.write(content.text)
fh.close

content.encoding = 'utf-8'
fh = open('u8ED.html', 'w')
fh.write(content.text)
fh.close

content.encoding = 'unicode'
fh = open('uniED.html', 'w')
fh.write(content.text)
fh.close

pattern = re.compile('snippets":[(.*?)]', re.S)
items = re.findall(pattern, content.text)
print (len(items))


