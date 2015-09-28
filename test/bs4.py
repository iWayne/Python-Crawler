from BeautifulSoup import BeautifulSoup


soup = BeautifulSoup(open("qsbk.html"))

print soup.title.string