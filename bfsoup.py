import urllib.request
from bs4 import BeautifulSoup

url="http://www.google.com"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())

#to print
print(soup.prettify())

#commands
soup.title
soup.title.name
soup.title.string
soup.title.parent.name
soup.p
soup.p['style']
soup.a
soup.find_all('a')
soup.find(id="link3")

#print all links
for link in soup.find_all('a'):
    print(link.get('href'))

#print all texts from doc
print(soup.get_text())

