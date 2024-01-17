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
show_banner()

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
        decoded_link = unquote(link)
        if search_term.lower() in decoded_link.lower(
        ) and "google.com" not in decoded_link and "/search?" not in decoded_link:
          links.append(decoded_link)
    return links
  else:
    print(f"Erro {response.status_code} na requisição de: {query}")
    return []


sensitive_filetypes = [
    'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'rtf', 'csv',
    'txt', 'sql', 'xml', 'conf', 'dat', 'ini', 'key', 'bak'
]

search_term = input(
    "Digite o termo que você deseja pesquisar: ").strip().lower()

for filetype in sensitive_filetypes:
  dork = f"{search_term} filetype:{filetype}"
  print(f"Executando pesquisa para filetype '{filetype}':")
  links = google_search(dork)

  if links:
    print(f"Links encontrados para {dork}:")
    for link in links:
      print(link)
  else:
    print(f"Nenhum resultado relevante encontrado para {dork}.")
  print("-" * 80)
