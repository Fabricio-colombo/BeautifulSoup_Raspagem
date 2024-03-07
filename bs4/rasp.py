import requests
from bs4 import BeautifulSoup as bs

link = 'https://www.google.com/search?q=cotacao+dolar'
requisicao = requests.get(link)
print(requisicao)
#print(requisicao.text)