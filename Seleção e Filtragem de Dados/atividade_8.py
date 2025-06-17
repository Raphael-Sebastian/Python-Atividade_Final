# 8. Selecione e exiba as colunas 'Produto', 'Categoria' e 'Preco_Kg'

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

produtos_selecionados = df_produtos[["Produto","Categoria","Preco_Kg"]]
print(f"\nDataFrame com Produto, Categoria e Preço_Kg")
print(produtos_selecionados.head())