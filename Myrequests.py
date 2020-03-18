import requests
from bs4 import BeautifulSoup

myBaidu = requests.get('https://tech.ifeng.com/c/7uwe8L6NZYm').content

# print(myBaidu)

Mysoup = BeautifulSoup(myBaidu, 'html.parser')
# print(Mysoup.text)

links = Mysoup.findAll('img')
# print(links)

for link in links:
    print(link)
    print(link.string)