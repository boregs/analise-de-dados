import pandas as pd
import matplotlib.pyplot as mtl

#projeto que pega dados de um banco de dados existente
#limpa os dados para que sobre só os necessarios
#cria uma visualizaçao desses dados

database = 'vendas_produtos.csv'
df_vendas = pd.read_csv(r'data_science\database\vendas_produtos.csv')

# ------------- LIMPANDO OS DADOS ------------------
# Formata as datas para o padrao DD/MM/AAAA
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'],format='mixed', dayfirst=True) 
df_vendas['data_venda'] = df_vendas['data_venda'].dt.strftime('%d/%m/%Y')# ambas linhas ajeitam a coluna da data das vendas para um padrao de DD/MM/AAAA

# tira a coluna 'id_venda'
df_vendas = df_vendas.drop(columns='id_venda') 

# preenche NaN na coluna 'quantidade' conforme o valor unitario e o valor final da venda
df_vendas['total_venda'] = pd.to_numeric(df_vendas['total_venda'], errors='coerce')
df_vendas['valor_unitario'] = pd.to_numeric(df_vendas['valor_unitario'], errors='coerce')

df_vendas['quantidade'] = df_vendas['quantidade'].fillna(df_vendas['total_venda'] / df_vendas['valor_unitario']) # divide o total de venda e o valor unitario de cada produto para retornar quantos produtos foram comprados e preenche as 
                                                                                                                 # partes que nao tem info
df_vendas['quantidade'] = df_vendas['quantidade'].astype(float) # converte para float

# preenche o NaN do valor unitario conforme a quantidade e o valor final da venda
df_vendas['total_venda'] = pd.to_numeric(df_vendas['total_venda'], errors='coerce')
df_vendas['valor_unitario'] = pd.to_numeric(df_vendas['valor_unitario'], errors='coerce')

df_vendas['valor_unitario'] = df_vendas['valor_unitario'].fillna(df_vendas['total_venda'] / df_vendas['quantidade'])

df_vendas['valor_unitario'] = df_vendas['valor_unitario'].astype(float) 

# remove duplicatas
df_vendas = df_vendas.drop_duplicates()

# ---------------- VISUALIZANDO OS DADOS -----------------------


