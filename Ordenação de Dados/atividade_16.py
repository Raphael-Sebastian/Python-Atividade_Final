# 16. Quais são os 5 produtos mais caros (maior Preco_Kg)?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

top_mais_caros = df_produtos.sort_values(by="Preco_Kg", ascending=False).head(5)
print(top_mais_caros)