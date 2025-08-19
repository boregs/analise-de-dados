import pandas as pd

database = 'teste.csv'
df = pd.read_csv(r'imersao alura\database\teste.csv')

print(df.isnull().sum()) # verifica se tem alguma parte da database que nao possui valor e mostra o total de informaçoes faltando
                         # em cada coluna da database

print(df['data_venda'].unique()) # coleta todas as informaçoes unicas dentro da coluna "data_venda"

print(df[df.isnull().any(axis=1)]) # baseicamente filtra na database todas as linhas que nao possuem informação e printa elas

