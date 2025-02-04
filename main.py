import requests 
import pandas as pd

url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'

response = requests.request(method='GET',url=url)
tabela = response.json()[0]['res']
dt = pd.DataFrame(tabela)
print(dt)