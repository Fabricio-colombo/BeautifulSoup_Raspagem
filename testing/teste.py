import random
import requests
from bs4 import BeautifulSoup as bs
import json

def token_temporario():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(10))

def realizar_consulta(client_data):
    token = token_temporario()

    url_login = f'https://consignadorapido.com/acesso/login_usuario?token_log={token}'

    headers_login = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://consignadorapido.com",
        "Referer": "https://consignadorapido.com/consulta/consultas",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "PHPSESSID=emamveuslp035r4pubb216c7k5"
    }

    data_login = {'login': '1009-LIS', 'senha': 'Lispro@2023'}
    response_login = requests.post(url_login, headers=headers_login, data=data_login)

    if response_login.status_code != 200:
        print("Falha ao fazer login. Código de status:", response_login.status_code)
        return

    url_consulta = f"https://consignadorapido.com/consulta/offline?token_log={token}"

    # Construir os dados para a consulta usando os dados do cliente
    data_consulta = {
        'higienizar': 0,
        'sistema': 'offline',
        'selectBC': 'cpf',
        'busca': client_data['dados_pessoais']['cpf'],
        'nascimento': client_data['dados_pessoais']['data_nascimento'],
        'valor_desejado': ''
    }

    response_consulta = requests.post(url_consulta, headers=headers_login, data=data_consulta)

    try:
        response_json = response_consulta.json()
        print("Status Code:", response_consulta.status_code)
        print("Response JSON:", response_json)
        beneficio = response_json['nb'][0].split(' ')[0]
        print("Benefício:", beneficio)
    except ValueError:
        print("Falha ao decodificar JSON, verificando a codificação da resposta.")
        try:
            decoded_content = response_consulta.content.decode('utf-8')
            response_json = json.loads(decoded_content)
            print("Decodificado e carregado com sucesso:", response_json)
        except Exception as e:
            print(f"Erro ao tentar decodificar a resposta: {e}")

# Dados do cliente fornecidos no segundo código
client_data = {
    "matriculas": [
        {
            "orgao": 1,
            "orgao_nome": "inss",
            "matricula": "123456789",
            "tipo": "32",
            "descricao": "tipo da matricula",
        }
    ],
    "telefones": [
        {
            "ddd": "48",
            "numero": "98165456",
            "score": 1,
            "data_info": "YYYY-MM-DD",
        },
        {
            "ddd": "48",
            "numero": "98168484",
            "score": 4,
            "data_info": "YYYY-MM-DD",
        },
    ],
    "enderecos": [
        {
            "uf": "sc",
            "cidade": "florianópolis",
            "cep": "88160000",
            "bairro": "centro",
            "endereco": "rua pedrinho",
            "numero": "80",
            "complemento": "",
            "score": 3,
            "data_info": "YYYY-MM-DD",
        }
    ],
    "dados_pessoais": {
        "nome": "pedro henrique campos",
        "outras_grafias_nome": ["pedro h campos", "pedro henrique"],
        "cpf": "46595465655",  # Sempre 11 dígitos
        "data_nascimento": "YYYY-MM-DD",
        "ppe": False,
        "nit": "4865254455",
        "nome_mae": "maria eduarda",
        "nome_pai": "mario jose",
        "dados_bancarios": [
            {
                "banco": "001",
                "tipo": "cc",
                "agencia": "1",
                "numero": "9512685",
                "digito": "2",
                "data_info": "YYYY-MM-DD",
                "score": 5,
            }
        ],
        "documentos": {
            "rg": {
                "data_expedicao": "YYYY-MM-DD",
                "orgao_expedicao": "ssp",
                "documento": "62456256",
                "data_validade": "YYYY-MM-DD",
                "uf": "sp",
            },
            "cnh": {
                "data_expedicao": "YYYY-MM-DD",
                "orgao_expedicao": "detran",
                "documento": "124123125",
                "data_validade": "YYYY-MM-DD",
                "uf": "sp",
            },
            "outros": [
                {
                    "tipo": "clt",
                    "data_expedicao": "YYYY-MM-DD",
                    "orgao_expedicao": "detran",
                    "documento": "124123125",
                    "data_validade": "YYYY-MM-DD",
                    "uf": "sp",
                }
            ],
        },
    },
    "message": "Processado com sucesso",
    "date": "YYYY-MM-DD HH-DD:SS",
    "usuario": "codigousuario",
}

# Chamar a função realizar_consulta com os dados do cliente
realizar_consulta(client_data)
