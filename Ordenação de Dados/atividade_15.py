#15. Liste todos os produtos ordenados alfabeticamente pelo nome.

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)


df_ordenando_por_nome = df_produtos.sort_values(by="Produto",ascending=True)
print("\n Lista por ordem alfabetica dos (Produto):")
print(df_ordenando_por_nome)