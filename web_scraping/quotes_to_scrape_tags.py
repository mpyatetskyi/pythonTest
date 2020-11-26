import requests
import bs4

url = 'https://quotes.toscrape.com/page/1/'
connection = requests.get(url)

soup = bs4.BeautifulSoup(connection.text,'lxml')

for item in  soup.select('.tag-item'):
    print(item.text)


