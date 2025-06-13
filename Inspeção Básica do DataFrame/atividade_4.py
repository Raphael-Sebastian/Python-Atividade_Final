# 4. Exiba as 7 primeiras linhas do DataFrame

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

print("primeiras 7 linhas do dataFrame de filmes")
print(df_produtos.head(7))
