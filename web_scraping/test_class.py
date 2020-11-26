import requests
import bs4

link = requests.get('https://en.wikipedia.org/wiki/Winston_Churchill')

soup = bs4.BeautifulSoup(link.text,'lxml')

#a = soup.select('.toctext')

#for i in a:
 #   print(i.getText())

#for item in soup.select('.toctext'):
#    print(item.text)
a = soup.select('img')

print(a)