import pandas as pd
import matplotlib.pyplot as plt

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
df_vendas.to_csv('vendas_produtos_limpo.csv', index=False)

# ---------------- VISUALIZANDO OS DADOS -----------------------

#df_vendas_limpo["metodo_pagamento"].value_counts().plot(kind='bar', title='Metodos de pagamento mais usados') pandas tambem faz graficos, isso é um exemplo

df_limpo = pd.read_csv(r'data_science\database\vendas_produtos_limpo.csv')

# rrotudos mais comprados
def tendencia_produtos_comprados():
    vendas_por_produto = df_vendas.groupby('nome_produto')['quantidade'].sum() # agrupa os produtos com suas respectivas quantidades de vendas dentro de toda database
    vendas_por_produto = vendas_por_produto.sort_values(ascending=False) # arruma em ordem decrescente

    produtos = vendas_por_produto.index # atribui os nomes dos produtos a variavel produto
    quantidades = vendas_por_produto.values # atribui a quantidade de venda total a variavel quantidade

    # o basico para criar um grafico de barras simples
    plt.figure(figsize=(8,5)) # ajeita o tamanho da figura
    plt.bar(produtos, quantidades, color='lightblue')
    plt.xlabel("Produtos")
    plt.ylabel("Quantidade de vendas")
    plt.title("Produtos mais comprados no mês de Julho")
    plt.xticks(produtos, rotation=45, fontsize=8) # rotaciona os nomes dos produtos no grafico e altera a fonte deles
    plt.show()

# metodo de pagamento mais usado
def metodo_pagamento():
    formas_pagamento = df_vendas.groupby('metodo_pagamento')['quantidade'].sum() # agrupa os produtos com suas respectivas quantidades de vendas dentro de toda database
    formas_pagamento = formas_pagamento.sort_values(ascending=False) # arruma em ordem decrescente

    forma = formas_pagamento.index # atribui os nomes dos produtos a variavel produto
    quantidade = formas_pagamento.values # atribui a quantidade de venda total a variavel quantidade

    # o basico para criar um grafico de barras simples
    plt.figure(figsize=(8,5)) # ajeita o tamanho da figura
    plt.bar(forma, quantidade, color='lightblue')
    plt.xlabel("Produtos")
    plt.ylabel("Quantidade de vendas")
    plt.title("Produtos mais comprados no mês de Julho")
    plt.xticks(forma, rotation=45, fontsize=8) # rotaciona os nomes dos produtos no grafico e altera a fonte deles
    plt.show()

