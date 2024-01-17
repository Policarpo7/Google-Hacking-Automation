#!/usr/bin/env python3
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup


def show_banner():
  print("=" * 50)
  print("  GOOGLE HACKING AUTOMATION")
  print("  Created by Gustavo Policarpo")
  print("=" * 50)

show_banner()

# Operadores de pesquisa do Google
google_hacking_operators = ['inurl:', 'intext:', 'intitle:', 'site:', 'cache:']

# Filetypes comumente associados a informações sensíveis
sensitive_filetypes = [
    'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'rtf', 'csv',
    'txt', 'sql', 'xml', 'conf', 'dat', 'ini', 'key', 'bak'
]


# Função para realizar buscas no Google
def google_search(query):
  headers = {'User-Agent': 'Mozilla/5.0'}
  params = {'q': query}
  response = requests.get(f"https://www.google.com/search?{urlencode(params)}",
                          headers=headers)

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a in soup.select('a[href^="/url?"]'):
      href = a['href']
      if href.startswith('/url?'):
        link = href.split('&')[0]
        link = link.split('=')[1]
        links.append(requests.utils.unquote(link))
    return links
  else:
    print(f"Erro {response.status_code} na requisição de: {query}")
    return []


# Função para imprimir os resultados de maneira organizada
def print_results(dork, links):
  print(f"Resultados para {dork}:")
  if links:
    for link in links:
      print(link)
  else:
    print("Nenhum link encontrado.")
  print("-" * 80)


# Solicita entrada do usuário para termo de busca
search_term = input("Digite o termo que você deseja pesquisar: ").strip()

# Executa a busca para cada operador de pesquisa
for operator in google_hacking_operators:
  dork = f"{operator}\"{search_term}\""
  links = google_search(dork)
  print_results(dork, links)

# Agora, executa a busca para cada filetype sensível
print("Pesquisando por filetypes sensíveis...")
for filetype in sensitive_filetypes:
  dork = f"filetype:{filetype} \"{search_term}\""
  links = google_search(dork)
  print_results(dork, links)
