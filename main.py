import requests 
import pandas as pd



def defineUrl(escolha, nome = None):
    if escolha == '1':
        url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'
    elif escolha == '2':
        url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    return url

escolha = ''
while escolha != '1' and escolha != '2':
    print('     - RANKING DE NOMES DO IBGE -     ')
    print('ESCOLHA UMA OPÇÃO: ')
    print('Opção 1 - Ver um ranking de nomes no geral')
    print('Opção 2 - Escolher um nome específico por década')
    escolha = input("Informe a opção desejada: ")
    if escolha == '2':
        nome = input("Informe o nome que deseja procurar: ")
    else: 
        nome = None

response = requests.request(method='GET',url=defineUrl(escolha,nome))
tabela = response.json()[0]['res']
df = pd.DataFrame(tabela)
print(df)