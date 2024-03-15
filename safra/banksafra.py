import requests
from bs4 import BeautifulSoup
import pprint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://epfweb.safra.com.br',
    'Referer': 'https://epfweb.safra.com.br/Home/Login',
}

data = {
    'CBU': 'CBU36005',
    'Senha': 'Consig@24'
}

url = 'https://epfweb.safra.com.br/'

session = requests.Session()

url = 'https://epfweb.safra.com.br/Home/Login?forcarLoginManual=S'

response = session.get(url, headers=headers)
print(response)
print(response.cookies.get_dict())


url = 'https://epfweb.safra.com.br/Home/Login'

response = requests.post(url, headers=headers, data=data)



if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    all_data = soup.find_all()
    pprint.pprint(all_data)
else:
    print('Failed to retrieve data. Status code:', response.status_code)
