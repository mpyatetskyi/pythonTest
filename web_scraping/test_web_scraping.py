import bs4
import requests
import lxml

result = requests.get('http://example.com/')

soup = bs4.BeautifulSoup(result.text,'lxml')


a = soup.select('p')[0].getText()

