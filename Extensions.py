#!/usr/bin/env python3
import requests
from urllib.parse import urlencode, unquote
from bs4 import BeautifulSoup

def show_banner():
    print("=" * 50)
    print("  GOOGLE HACKING AUTOMATION")
    print("  Created by Gustavo Policarpo")
    print("=" * 50)

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
                # Filtra links indesejados
                if all(x not in decoded_link for x in ['maps.google.com', 'support.google.com', 'accounts.google.com']):
                    links.append(decoded_link)
        return links
    else:
        print(f"Erro {response.status_code} na requisição de: {query}")
        return []

# Função para imprimir os resultados de maneira organizada
def print_results(dork, links, search_term):
    print(f"Resultados para {dork}:")
    found = False
    for link in links:
        if search_term.lower().replace("\"", "") in link.lower():
            print(link)
            found = True
    if not found:
        print("Nenhum resultado exato encontrado para a sua pesquisa.")
    print("-" * 80)

# Solicita entrada do usuário para termo de busca
search_term = input("Digite o termo que você deseja pesquisar: ").strip()

# Adiciona aspas ao redor do termo de pesquisa para busca exata
search_term_quoted = f"\"{search_term}\""

# Executa a busca para cada operador de pesquisa
for operator in google_hacking_operators:
    dork = f"{operator}{search_term_quoted}"
    links = google_search(dork)
    print_results(dork, links, search_term)
