import requests 
import pandas as pd
from rich.console import Console
from rich.table import Table


def defineUrl(escolha, nome = None, decada= None, localidade = None, sexo = None):
    baseUrl = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/'

    if escolha == '1':
        url = f'{baseUrl}ranking'
        params = {}
        if decada:
            params['decada'] = decada

        if localidade:
            params['localidade'] = localidade   

        if sexo:
            params["sexo"] = sexo
    
    elif escolha == '2':
        url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
        params = {}

        if localidade:
            params['localidade'] = localidade   

        if sexo:
            params["sexo"] = sexo
    
    return url, params

def display_data(df):
    console = Console()
    table = Table(title="\nResultados da Consulta")

    for column in df.columns:
        table.add_column(column)

    for _, row in df.iterrows():
        table.add_row(*[str(row[column]) for column in df.columns])

    console.print(table)


def main():
    escolha = ''
    while escolha != '1' and escolha != '2':
        print('     - RANKING DE NOMES DO IBGE -     ')
        print('ESCOLHA UMA OPÇÃO: ')
        print('Opção 1 - Ver um ranking de nomes no geral')
        print('Opção 2 - Escolher um nome específico por década')
        escolha = input("Informe a opção desejada: ")
        
        if escolha == '2':
            nome = input("Informe o nome que deseja procurar: ")
            localidade = input("Informe uma localidade específica para procurar (OPCIONAL): ")
            sexo = input("Informe um sexo para procurar (M ou F)(OPCIONAL): ").upper()
            decada = None

        elif escolha == '1':
            decada = input("Informe uma decada específica para procurar (OPCIONAL): ")
            localidade = input("Informe uma localidade específica para procurar (OPCIONAL): ")
            sexo = input("Informe um sexo para procurar (M ou F)(OPCIONAL): ").upper() 
            nome = None

    url, params = defineUrl(escolha,nome,decada,localidade,sexo)




    try:    
        response = requests.request(method='GET',url=url, params=params)
        tabela = response.json()[0]['res']
        df = pd.DataFrame(tabela)
        display_data(df)
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    main()