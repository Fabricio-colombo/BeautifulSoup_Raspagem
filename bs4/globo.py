import requests
from bs4 import BeautifulSoup as bs

link = 'https://www.globo.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

response = requests.get(link, headers=headers)

if response.status_code == 200:
    site = bs(response.text, 'html.parser')
    
    titulo = site.find('title').text.strip()
    print(f"Título da página: {titulo}")
    
    jornalismo = site.find('div', class_='topglobocom__ranking theme-jornalismo').text.strip()
    print(f"Sub-Titulo Noticias: {jornalismo}")
    
else:
    print(f'Erro: {response.status_code}')    