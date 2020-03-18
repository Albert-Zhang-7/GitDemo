import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.baidu.com/').content
soup = BeautifulSoup(data, 'html.parser')
# print(soup.text)
print(soup.title)
print(soup.title.string)
print(soup.body)
print(soup.body.div)
print(soup.body.div.attrs)
