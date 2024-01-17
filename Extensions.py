#!/usr/bin/env python3
import requests
from urllib.parse import urlencode, unquote
from bs4 import BeautifulSoup

def show_banner():
    banner = """
+-------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                 |
|                                                                                                                                                 |
|   ____  ___   ___   ____ _     _____   _   _    _    ____ _  _____ _   _  ____      _   _   _ _____ ___  __  __    _  _____ ___ ___  _   _      |
|  / ___|/ _ \ / _ \ / ___| |   | ____| | | | |  / \  / ___| |/ /_ _| \ | |/ ___|    / \ | | | |_   _/ _ \|  \/  |  / \|_   _|_ _/ _ \| \ | |     |
| | |  _| | | | | | | |  _| |   |  _|   | |_| | / _ \| |   | ' / | ||  \| | |  _    / _ \| | | | | || | | | |\/| | / _ \ | |  | | | | |  \| |     |
| | |_| | |_| | |_| | |_| | |___| |___  |  _  |/ ___ \ |___| . \ | || |\  | |_| |  / ___ \ |_| | | || |_| | |  | |/ ___ \| |  | | |_| | |\  |     |
|  \____|\___/ \___/ \____|_____|_____| |_| |_/_/   \_\____|_|\_\___|_| \_|\____| /_/   \_\___/  |_| \___/|_|  |_/_/   \_\_| |___\___/|_| \_|     |
|                                                                                                                                                 |        
|                                                                                                                                                 |                              
|                                                                                                                                                 |
|                                                                                                                                                 |
|                   by Gustavo Policarpo                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------+
    """
    print(banner)

show_banner()

# Operadores de pesquisa do Google
google_hacking_operators = ['inurl:', 'intext:', 'intitle:', 'site:', 'cache:']

# Função para realizar buscas no Google
def google_search(query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'q': query}
    response = requests.get(f"https://www.google.com/search?{urlencode(params)}", headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for a in soup.select('a[href^="/url?"]'):
            href = a['href']
            if href.startswith('/url?'):
                link = href.split('&')[0]
                link = link.split('=')[1]
                decoded_link = unquote(link)
                # Filtra links indesejados e links de nova pesquisa
                if all(x not in decoded_link for x in ['maps.google.com', 'support.google.com', 'accounts.google.com', '/search?q=']):
                    links.append(decoded_link)
        return links
    else:
        print(f"Erro {response.status_code} na requisição de: {query}")
        return []

# Função para imprimir os resultados de maneira organizada
def print_results(dork, links):
    print(f"\nResultados para {dork}:")
    if links:
        for link in links:
            print(link)
    else:
        print("Nenhum resultado relevante encontrado.")
    print("-" * 80)

# Solicita entrada do usuário para termo de busca
search_term = input("Digite o termo que você deseja pesquisar: ").strip()

# Adiciona aspas ao redor do termo de pesquisa para busca exata
search_term_quoted = f"\"{search_term}\""

# Executa a busca para cada operador de pesquisa
for operator in google_hacking_operators:
    dork = f"{operator}{search_term_quoted}"
    links = google_search(dork)
    print_results(dork, links)
