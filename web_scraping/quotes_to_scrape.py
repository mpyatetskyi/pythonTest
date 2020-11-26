import requests
import bs4

url = 'https://quotes.toscrape.com/page/{}/'
connection = requests.get(url)

soup = bs4.BeautifulSoup(connection.text,'lxml')

myset = set()


for n in range(1,11):
    scrap_url = url.format(n)
    res = requests.get(scrap_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    for author in soup.select('.author'):
        myset.add(author.text)


for i in myset:
    print(i)