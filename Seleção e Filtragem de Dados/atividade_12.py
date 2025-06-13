# 12. Quais produtos foram repostos no dia '2024-06-01'?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

reposicao_dia = df_produtos[df_produtos["Data_Ultima_Reposicao"] == "2024-06-01"]
print("\nProdutos repostos em 2024-06-01:")
print(reposicao_dia)