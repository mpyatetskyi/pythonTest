import requests
import bs4

link = requests.get('https://ru.wikipedia.org/wiki/Stone_Sour')

soup = bs4.BeautifulSoup(link.text,'lxml')



#for item in soup.select('.thumbimage'):
#    print(item)

#myimage = soup.select('.thumbimage')[0]
#print('\n'*2)
#print(myimage['src'])

my_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Stone_Sour_%285%29.JPG/250px-Stone_Sour_%285%29.JPG')


print(my_link.text)
#f = open('C:/Users/Lenovo/Desktop/my_immage.jpeg','wb')
#f.write(my_link.content)
#f.close()