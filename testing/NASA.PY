import requests
from bs4 import BeautifulSoup as bs

link = 'https://www.nasa.gov/2024-news-releases/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
response = requests.get(link, headers=headers)

print(response.status_code)

if response.status_code == 200:
    site = bs(response.text, 'html.parser')
    
    titulos = site.find_all('div', class_='hds-a11y-heading-22')
    paragrafos = site.find_all('p', class_='margin-top-0 margin-bottom-1')
    
    for titulo, paragrafo in zip(titulos, paragrafos):
        print(f'Título da notícia: {titulo.text.strip()}')
        print(f'Conteúdo da notícia: {paragrafo.text.strip()}')
        print()
else:
    print("Erro ao acessar a página:", response.status_code)