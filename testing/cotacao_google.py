import requests
from bs4 import BeautifulSoup as bs

link = 'https://www.google.com/search?q=cotacao+dolar'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
response = requests.get(link, headers=headers)

if response.status_code == 200:
    site = bs(response.text, 'html.parser')
    
    titulo = site.find('title').text.strip()
    print(f"Título da página: {titulo}")
    
    cotacao = site.find('div', class_="b1hJbf").text.strip()
    print(f"Cotação do dólar: {cotacao}")
        
    
else:
    print("Erro ao acessar a página:", response.status_code)
