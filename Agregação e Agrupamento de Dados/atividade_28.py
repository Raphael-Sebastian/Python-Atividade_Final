# 28. Qual o número de produtos distintos fornecidos por cada Fornecedor?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

produtos_distintos = df_produtos.groupby('Fornecedor')['Produto'].nunique() #['Produto'].nunique() == conta quantos produtos únicos cada fornecedor tem.
print(produtos_distintos)
