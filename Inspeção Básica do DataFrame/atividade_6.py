# 6. Obtenha um resumo estatístico das colunas numéricas (como preço e estoque).


import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

resumo = df_produtos.describe()
print(resumo)
