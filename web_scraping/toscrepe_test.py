import requests
import bs4

url = 'https://books.toscrape.com/catalogue/page-{}.html'

two_star_title = []

for n in range(1,51):
    scrape_url = url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            my_book = book.select('a')[1]['title']
            two_star_title.append(my_book)


print(two_star_title)