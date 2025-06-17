# 11. Quais frutas têm um Preco_Kg superior a R$ 10,00?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

df_produtos["Preco_Kg"] = pd.to_numeric(df_produtos["Preco_Kg"], errors="coerce")

produtos_selecionados = df_produtos[df_produtos["Preco_Kg"] > 10.00]
print(f"\nProdutos com preço acima de R$ 10,00")
print(produtos_selecionados.head())
